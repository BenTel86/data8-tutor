"""Build and load a BM25 index, with optional provider embeddings."""

from __future__ import annotations

import json
import pickle
import re
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path

from rank_bm25 import BM25Okapi

from .chunk import Chunk, chunk_corpus
from .corpus import iter_corpus_files
from .llm import create_llm_client, load_llm_config
from .paths import (
    BM25_PATH,
    CHUNKS_PATH,
    EMBEDDINGS_PATH,
    INDEX_DIR,
    META_PATH,
)

TOKEN = re.compile(r"[a-z0-9_.]+")


def tokenize(text: str) -> list[str]:
    tokens = TOKEN.findall(text.lower())
    extra: list[str] = []
    for tok in tokens:
        if "." in tok or "_" in tok:
            extra.extend(part for part in re.split(r"[._]+", tok) if part)
    return tokens + extra


def _ensure_index_dir() -> None:
    INDEX_DIR.mkdir(parents=True, exist_ok=True)


def _write_jsonl(path: Path, rows: list[dict]) -> None:
    with path.open("w", encoding="utf-8") as handle:
        for row in rows:
            handle.write(json.dumps(row, ensure_ascii=False) + "\n")


def _read_jsonl(path: Path) -> list[dict]:
    if not path.exists():
        return []
    rows: list[dict] = []
    with path.open(encoding="utf-8") as handle:
        for line in handle:
            line = line.strip()
            if line:
                rows.append(json.loads(line))
    return rows


def _embed_texts(texts: list[str], model: str) -> list[list[float]]:
    client = create_llm_client()
    vectors: list[list[float]] = []
    batch_size = 64
    for start in range(0, len(texts), batch_size):
        batch = texts[start : start + batch_size]
        response = client.embeddings.create(model=model, input=batch)
        by_index = {item.index: item.embedding for item in response.data}
        vectors.extend(by_index[i] for i in range(len(batch)))
    return vectors


def build_index(*, embed: bool = False, embedding_model: str | None = None) -> dict:
    _ensure_index_dir()
    files = iter_corpus_files()
    chunks = chunk_corpus(files, include_staff=True)
    rows = [chunk.to_dict() for chunk in chunks]
    _write_jsonl(CHUNKS_PATH, rows)

    tokenized = [tokenize(chunk.text) for chunk in chunks]
    bm25 = BM25Okapi(tokenized)
    BM25_PATH.write_bytes(pickle.dumps(bm25))

    embedding_count = 0
    resolved_embedding_model = None
    if embed:
        resolved_embedding_model = (
            embedding_model or load_llm_config().embedding_model
        )
        vectors = _embed_texts([chunk.text for chunk in chunks], resolved_embedding_model)
        _write_jsonl(
            EMBEDDINGS_PATH,
            [{"id": chunk.id, "vector": vector} for chunk, vector in zip(chunks, vectors)],
        )
        embedding_count = len(vectors)
    elif EMBEDDINGS_PATH.exists():
        EMBEDDINGS_PATH.unlink()

    meta = {
        "built_at": datetime.now(timezone.utc).isoformat(),
        "files": len(files),
        "chunks": len(chunks),
        "student_chunks": sum(1 for chunk in chunks if chunk.audience == "student"),
        "staff_chunks": sum(1 for chunk in chunks if chunk.audience == "staff"),
        "embeddings": embedding_count,
        "embedding_model": resolved_embedding_model,
    }
    META_PATH.write_text(json.dumps(meta, indent=2), encoding="utf-8")
    return meta


def index_exists() -> bool:
    return CHUNKS_PATH.exists() and BM25_PATH.exists()


def load_meta() -> dict:
    if not META_PATH.exists():
        return {}
    return json.loads(META_PATH.read_text(encoding="utf-8"))


@dataclass
class Hit:
    chunk: Chunk
    score: float


def _dot(a: list[float], b: list[float]) -> float:
    return sum(x * y for x, y in zip(a, b))


def _norm(a: list[float]) -> float:
    return sum(x * x for x in a) ** 0.5


def _cosine(a: list[float], b: list[float]) -> float:
    denom = _norm(a) * _norm(b)
    if denom == 0:
        return 0.0
    return _dot(a, b) / denom


def _rrf(rank_lists: list[list[str]], k: int = 60) -> dict[str, float]:
    scores: dict[str, float] = {}
    for ranking in rank_lists:
        for rank, chunk_id in enumerate(ranking):
            scores[chunk_id] = scores.get(chunk_id, 0.0) + 1.0 / (k + rank + 1)
    return scores


def _kind_weight(query: str, kind: str) -> float:
    lowered = query.lower()
    exam_query = any(word in lowered for word in ("exam", "midterm", "final"))
    if kind == "exam" and not exam_query:
        return 0.5
    return 1.0


def retrieve(query: str, *, staff: bool = False, k: int = 8) -> list[Hit]:
    if not index_exists():
        raise FileNotFoundError(
            "No tutor index yet. Run `python -m tutor ingest` from the repo root."
        )
    rows = _read_jsonl(CHUNKS_PATH)
    chunks = [Chunk(**row) for row in rows]
    allowed = {
        i
        for i, chunk in enumerate(chunks)
        if staff or chunk.audience == "student"
    }
    bm25: BM25Okapi = pickle.loads(BM25_PATH.read_bytes())
    bm25_scores = bm25.get_scores(tokenize(query))
    bm25_ranked = sorted(
        (i for i in allowed),
        key=lambda i: bm25_scores[i] * _kind_weight(query, chunks[i].kind),
        reverse=True,
    )
    rank_lists = [[chunks[i].id for i in bm25_ranked[:40]]]

    if EMBEDDINGS_PATH.exists():
        config = load_llm_config()
        model = load_meta().get("embedding_model") or config.embedding_model
        client = create_llm_client(config)
        query_vec = client.embeddings.create(model=model, input=[query]).data[0].embedding
        vectors = {row["id"]: row["vector"] for row in _read_jsonl(EMBEDDINGS_PATH)}
        dense_ranked = sorted(
            (i for i in allowed if chunks[i].id in vectors),
            key=lambda i: _cosine(query_vec, vectors[chunks[i].id]),
            reverse=True,
        )
        rank_lists.append([chunks[i].id for i in dense_ranked[:40]])

    fused = _rrf(rank_lists)
    ordered_ids = sorted(fused, key=fused.get, reverse=True)
    by_id = {chunk.id: chunk for chunk in chunks}
    hits: list[Hit] = []
    for chunk_id in ordered_ids:
        if chunk_id not in by_id:
            continue
        chunk = by_id[chunk_id]
        if not staff and chunk.audience != "student":
            continue
        hits.append(Hit(chunk=chunk, score=fused[chunk_id]))
        if len(hits) >= k:
            break
    return hits
