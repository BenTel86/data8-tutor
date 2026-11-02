"""Shared tutor API: retrieve corpus chunks, then ask the LLM."""

from __future__ import annotations

from dataclasses import dataclass, field

from .index import Hit, retrieve
from .llm import create_llm_client, load_llm_config
from .prompt import system_prompt


@dataclass
class TutorReply:
    text: str
    sources: list[str] = field(default_factory=list)
    hits: list[Hit] = field(default_factory=list)


def _format_context(hits: list[Hit]) -> str:
    blocks = []
    for i, hit in enumerate(hits, start=1):
        chunk = hit.chunk
        blocks.append(
            f"SOURCE {i}: {chunk.source} ({chunk.kind}, {chunk.audience})"
            f"\n{chunk.text}"
        )
    return "\n\n----\n\n".join(blocks)


def _unique_sources(hits: list[Hit]) -> list[str]:
    seen: list[str] = []
    for hit in hits:
        source = hit.chunk.source
        if source not in seen:
            seen.append(source)
    return seen


def answer(
    question: str,
    *,
    history: list[dict[str, str]] | None = None,
    staff: bool = False,
    model: str | None = None,
    k: int = 8,
) -> TutorReply:
    """Return a tutoring reply grounded in md_corpus. Platform bots should call this."""
    llm_config = load_llm_config()

    hits = retrieve(question, staff=staff, k=k)
    sources = _unique_sources(hits)
    context = _format_context(hits) if hits else "(no matching course files)"
    user_block = (
        f"Retrieved course material:\n\n{context}\n\n"
        f"Student question:\n{question.strip()}"
    )
    messages: list[dict[str, str]] = [{"role": "system", "content": system_prompt(staff)}]
    if history:
        messages.extend(history)
    messages.append({"role": "user", "content": user_block})

    client = create_llm_client(llm_config)
    response = client.chat.completions.create(
        model=model or llm_config.chat_model,
        messages=messages,
        temperature=0.3,
    )
    text = (response.choices[0].message.content or "").strip()
    return TutorReply(text=text, sources=sources, hits=hits)
