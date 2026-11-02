"""Data 8 tutor website. Streamlit Community Cloud runs this file."""

from __future__ import annotations

import os

import streamlit as st
from dotenv import load_dotenv

from tutor.engine import answer
from tutor.index import build_index, index_exists
from tutor.llm import load_llm_config
from tutor.paths import ROOT
from tutor.site import MAX_QUESTION_CHARS, apply_cloud_secrets, trim_history

st.set_page_config(page_title="Data 8 Tutor", layout="centered")

load_dotenv(ROOT / ".env")
os.chdir(ROOT)
try:
    apply_cloud_secrets(os.environ, st.secrets)
except Exception:
    pass


@st.cache_resource(show_spinner="Indexing course materials...")
def _ready() -> bool:
    if not index_exists():
        build_index()
    load_llm_config()
    return True


st.title("Data 8 Tutor")
st.markdown(
    "A course tutor for UC Berkeley Data 8. Ask about homework, labs, "
    "lectures, or projects. It answers from the course materials and stays "
    "in student mode, so it will not hand over solutions."
)

try:
    _ready()
except Exception as exc:
    st.error(str(exc))
    st.stop()

if "messages" not in st.session_state:
    st.session_state.messages = []
if "history" not in st.session_state:
    st.session_state.history = []

if not st.session_state.messages:
    st.info('Ask a question below. For example: "How do I use tbl.where?"')

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])
        sources = message.get("sources") or []
        if sources:
            st.caption("Sources: " + ", ".join(f"`{source}`" for source in sources[:8]))

question = st.chat_input("Ask a Data 8 question")
if not question:
    st.stop()

question = " ".join(question.split())
if not question:
    st.stop()
if len(question) > MAX_QUESTION_CHARS:
    st.error(f"Question is too long (max {MAX_QUESTION_CHARS} characters).")
    st.stop()

st.session_state.messages.append({"role": "user", "content": question, "sources": []})
with st.chat_message("user"):
    st.markdown(question)

with st.chat_message("assistant"):
    with st.spinner("Thinking..."):
        try:
            reply = answer(
                question,
                history=list(st.session_state.history),
                staff=False,
            )
        except Exception as exc:
            st.error(f"Tutor failed: {exc}")
            st.stop()
    st.markdown(reply.text)
    if reply.sources:
        st.caption("Sources: " + ", ".join(f"`{source}`" for source in reply.sources[:8]))

st.session_state.messages.append(
    {"role": "assistant", "content": reply.text, "sources": reply.sources}
)
st.session_state.history.append({"role": "user", "content": question})
st.session_state.history.append({"role": "assistant", "content": reply.text})
st.session_state.history = trim_history(st.session_state.history)
