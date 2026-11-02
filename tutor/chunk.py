"""Split Markdown into retrieval chunks, keeping headings with the body."""

from __future__ import annotations

import re
from dataclasses import asdict, dataclass

from .corpus import CorpusFile, parse_front_matter, strip_for_student

HEADING = re.compile(r"(?m)^(#{2,3} .+)$")
MAX_CHARS = 3500
MIN_CHARS = 120


@dataclass
class Chunk:
    id: str
    text: str
    source: str
    kind: str
    audience: str
    title: str
    heading: str

    def to_dict(self) -> dict[str, str]:
        return asdict(self)


def _split_oversized(text: str, max_chars: int) -> list[str]:
    if len(text) <= max_chars:
        return [text]
    parts: list[str] = []
    buf: list[str] = []
    size = 0
    for para in text.split("\n\n"):
        extra = len(para) + 2
        if buf and size + extra > max_chars:
            parts.append("\n\n".join(buf).strip())
            buf = [para]
            size = extra
        else:
            buf.append(para)
            size += extra
    if buf:
        parts.append("\n\n".join(buf).strip())
    out: list[str] = []
    for part in parts:
        if len(part) <= max_chars:
            if part:
                out.append(part)
            continue
        for start in range(0, len(part), max_chars):
            piece = part[start : start + max_chars].strip()
            if piece:
                out.append(piece)
    return out


def _sections(body: str) -> list[tuple[str, str]]:
    matches = list(HEADING.finditer(body))
    if not matches:
        return [("", body.strip())]
    sections: list[tuple[str, str]] = []
    if matches[0].start() > 0:
        lead = body[: matches[0].start()].strip()
        if lead:
            sections.append(("", lead))
    for i, match in enumerate(matches):
        end = matches[i + 1].start() if i + 1 < len(matches) else len(body)
        heading = match.group(1).strip()
        content = body[match.end() : end].strip()
        sections.append((heading, f"{heading}\n\n{content}".strip()))
    return sections


def chunk_file(file: CorpusFile, audience: str) -> list[Chunk]:
    raw = file.path.read_text(encoding="utf-8")
    meta, body = parse_front_matter(raw)
    if audience == "student":
        if file.staff_only:
            return []
        body = strip_for_student(body, file.kind)
    title = meta.get("title") or file.meta.get("title") or file.path.stem
    chunks: list[Chunk] = []
    index = 0
    for heading, section in _sections(body):
        for piece in _split_oversized(section, MAX_CHARS):
            if len(piece) < MIN_CHARS and chunks:
                prev = chunks[-1]
                merged = f"{prev.text}\n\n{piece}"
                if len(merged) <= MAX_CHARS * 1.5:
                    chunks[-1] = Chunk(
                        id=prev.id,
                        text=merged,
                        source=prev.source,
                        kind=prev.kind,
                        audience=prev.audience,
                        title=prev.title,
                        heading=prev.heading or heading,
                    )
                    continue
            labels = [file.kind, title]
            if heading:
                labels.append(heading)
            prefix = f"[{' | '.join(labels)}]\n{file.relative}\n\n"
            chunks.append(
                Chunk(
                    id=f"{file.relative}#{audience}#{index}",
                    text=prefix + piece.strip(),
                    source=file.relative,
                    kind=file.kind,
                    audience=audience,
                    title=title,
                    heading=heading,
                )
            )
            index += 1
    return chunks


def chunk_corpus(files: list[CorpusFile], include_staff: bool = True) -> list[Chunk]:
    chunks: list[Chunk] = []
    for file in files:
        if file.staff_only:
            if include_staff:
                chunks.extend(chunk_file(file, "staff"))
            continue
        chunks.extend(chunk_file(file, "student"))
        if include_staff and file.kind in {"homework", "lab", "project"}:
            chunks.extend(chunk_file(file, "staff"))
    return chunks
