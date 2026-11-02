"""LLM provider configuration shared by chat and embedding calls."""

from __future__ import annotations

import os
from dataclasses import dataclass
from typing import Mapping

OPENROUTER_BASE_URL = "https://openrouter.ai/api/v1"
DEFAULT_OPENROUTER_MODEL = "openai/gpt-4o-mini"
DEFAULT_OPENAI_MODEL = "gpt-4o-mini"


@dataclass(frozen=True)
class LLMConfig:
    provider: str
    api_key: str
    base_url: str | None
    chat_model: str
    embedding_model: str
    default_headers: dict[str, str]


def load_llm_config(environ: Mapping[str, str] | None = None) -> LLMConfig:
    """Resolve OpenRouter first, with OpenAI retained as a supported fallback."""
    env = os.environ if environ is None else environ
    provider = env.get("LLM_PROVIDER", "").strip().lower()
    if not provider:
        if env.get("OPENROUTER_API_KEY", "").strip():
            provider = "openrouter"
        elif env.get("OPENAI_API_KEY", "").strip():
            provider = "openai"
        else:
            raise RuntimeError(
                "No LLM API key is configured. Set OPENROUTER_API_KEY "
                "(recommended) or OPENAI_API_KEY in .env."
            )

    if provider == "openrouter":
        api_key = env.get("OPENROUTER_API_KEY", "").strip()
        if not api_key:
            raise RuntimeError(
                "LLM_PROVIDER is openrouter but OPENROUTER_API_KEY is not set."
            )
        headers = {}
        if env.get("OPENROUTER_SITE_URL", "").strip():
            headers["HTTP-Referer"] = env["OPENROUTER_SITE_URL"].strip()
        if env.get("OPENROUTER_APP_NAME", "").strip():
            headers["X-OpenRouter-Title"] = env["OPENROUTER_APP_NAME"].strip()
        return LLMConfig(
            provider=provider,
            api_key=api_key,
            base_url=env.get("OPENROUTER_BASE_URL", "").strip()
            or OPENROUTER_BASE_URL,
            chat_model=env.get("OPENROUTER_MODEL", "").strip()
            or DEFAULT_OPENROUTER_MODEL,
            embedding_model=env.get("OPENROUTER_EMBEDDING_MODEL", "").strip()
            or "openai/text-embedding-3-small",
            default_headers=headers,
        )

    if provider == "openai":
        api_key = env.get("OPENAI_API_KEY", "").strip()
        if not api_key:
            raise RuntimeError("LLM_PROVIDER is openai but OPENAI_API_KEY is not set.")
        return LLMConfig(
            provider=provider,
            api_key=api_key,
            base_url=env.get("OPENAI_BASE_URL", "").strip() or None,
            chat_model=env.get("OPENAI_MODEL", "").strip() or DEFAULT_OPENAI_MODEL,
            embedding_model=env.get("OPENAI_EMBEDDING_MODEL", "").strip()
            or "text-embedding-3-small",
            default_headers={},
        )

    raise RuntimeError("LLM_PROVIDER must be either 'openrouter' or 'openai'.")


def create_llm_client(config: LLMConfig | None = None):
    """Create an OpenAI-compatible client for the configured provider."""
    from openai import OpenAI

    resolved = config or load_llm_config()
    kwargs: dict[str, object] = {"api_key": resolved.api_key}
    if resolved.base_url:
        kwargs["base_url"] = resolved.base_url
    if resolved.default_headers:
        kwargs["default_headers"] = resolved.default_headers
    return OpenAI(**kwargs)
