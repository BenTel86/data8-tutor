"""Repo-relative locations for the corpus and the built index."""

from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CORPUS_DIR = ROOT / "md_corpus"
DATA_DIR = ROOT / "tutor_data"
INDEX_DIR = DATA_DIR / "index"
CHUNKS_PATH = INDEX_DIR / "chunks.jsonl"
BM25_PATH = INDEX_DIR / "bm25.pkl"
EMBEDDINGS_PATH = INDEX_DIR / "embeddings.jsonl"
META_PATH = INDEX_DIR / "meta.json"
