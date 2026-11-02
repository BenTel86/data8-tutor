"""Discover md_corpus Markdown files and strip staff-only material."""

from __future__ import annotations

import re
from dataclasses import dataclass
from pathlib import Path

from .paths import CORPUS_DIR

COMBINED_NAMES = {
    "hw.md",
    "lab.md",
    "project.md",
    "data8-sp26-solutions.md",
    "data8-sp26-textbook.md",
    "data8-sp26-lectures.md",
    "data8-sp26-exams.md",
    "tutoring_worksheets.md",
    "discussion_worksheets.md",
    "license.md",
    "provenance.md",
    "readme.md",
}

SOLUTION_HEADING = re.compile(
    r"\*\*Solution:\*\*\s*\n+(?:```[\s\S]*?```\s*)?",
    re.IGNORECASE,
)
TEST_HEADING = re.compile(
    r"\*\*Test[^*]*\*\*\s*\n+(?:```[\s\S]*?```\s*)?",
    re.IGNORECASE,
)
OUTPUT_HEADING = re.compile(
    r"\*Output:\*\s*\n+(?:```[\s\S]*?```\s*)?",
    re.IGNORECASE,
)
BEGIN_SOLUTION = re.compile(
    r"[ \t]*# BEGIN SOLUTION(?: NO PROMPT)?\s*\n[\s\S]*?[ \t]*# END SOLUTION\s*\n?",
    re.IGNORECASE,
)
SOLUTION_LINE = re.compile(r"^.*# SOLUTION(?: NO PROMPT)?.*\n?", re.MULTILINE)
FRONT_MATTER = re.compile(r"\A---\n(.*?)\n---\n?", re.DOTALL)

KIND_FROM_PART = {
    "textbook": "textbook",
    "lectures": "lecture",
    "homework": "homework",
    "lab": "lab",
    "project": "project",
    "exam": "exam",
    "discussions": "discussion",
    "tutoring": "tutoring",
}


@dataclass(frozen=True)
class CorpusFile:
    path: Path
    relative: str
    kind: str
    staff_only: bool
    meta: dict[str, str]


def is_combined_file(path: Path) -> bool:
    return path.name.lower() in COMBINED_NAMES


def is_solution_file(path: Path) -> bool:
    stem = path.stem
    return stem.endswith("-sol") or stem.endswith("_Sol") or stem.endswith("_sol")


def kind_for(path: Path) -> str:
    parts = {part.lower() for part in path.parts}
    for part, kind in KIND_FROM_PART.items():
        if part in parts:
            return kind
    return "other"


def parse_front_matter(text: str) -> tuple[dict[str, str], str]:
    match = FRONT_MATTER.match(text)
    if not match:
        return {}, text
    meta: dict[str, str] = {}
    for line in match.group(1).splitlines():
        if ":" not in line or line.startswith(" ") or line.startswith("-"):
            continue
        key, value = line.split(":", 1)
        meta[key.strip()] = value.strip().strip('"').strip("'")
    return meta, text[match.end() :].lstrip("\n")


def strip_for_student(text: str, kind: str) -> str:
    """Remove staff answers from assignment-style files. Other kinds pass through."""
    if kind not in {"homework", "lab", "project"}:
        return text
    body = SOLUTION_HEADING.sub("", text)
    body = TEST_HEADING.sub("", body)
    body = OUTPUT_HEADING.sub("", body)
    body = BEGIN_SOLUTION.sub("", body)
    body = SOLUTION_LINE.sub("", body)
    return re.sub(r"\n{3,}", "\n\n", body).strip() + "\n"


def iter_corpus_files(corpus_dir: Path | None = None) -> list[CorpusFile]:
    root = corpus_dir or CORPUS_DIR
    files: list[CorpusFile] = []
    for path in sorted(root.rglob("*.md")):
        if is_combined_file(path):
            continue
        relative = path.relative_to(root).as_posix()
        kind = kind_for(path)
        raw = path.read_text(encoding="utf-8")
        meta, _ = parse_front_matter(raw)
        files.append(
            CorpusFile(
                path=path,
                relative=relative,
                kind=kind,
                staff_only=is_solution_file(path),
                meta=meta,
            )
        )
    return files
