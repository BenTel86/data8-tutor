"""Shared helpers for the Streamlit website. Student mode only."""

from __future__ import annotations

from typing import Mapping, MutableMapping

HISTORY_TURNS = 8
MAX_QUESTION_CHARS = 2000


def apply_cloud_secrets(
    environ: MutableMapping[str, str],
    secrets: Mapping[str, object],
) -> None:
    """Copy Streamlit secrets into the process env without overwriting local .env."""
    for key, value in secrets.items():
        if not isinstance(value, str):
            continue
        text = value.strip()
        if text and not str(environ.get(key, "")).strip():
            environ[key] = text


def trim_history(history: list[dict[str, str]], turns: int = HISTORY_TURNS) -> list[dict[str, str]]:
    return history[-turns:]
