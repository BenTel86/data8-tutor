# Data 8 Tutor

A one-page website: intro plus a chatbot that answers Data 8 questions from the course corpus. Student mode only.

## Local

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
copy .env.example .env
```

Put your OpenRouter key in `.env`, then:

```bash
streamlit run streamlit_app.py
```

## Streamlit Cloud (public URL, free hosting)

1. Push this folder to a GitHub repo.
2. Open [share.streamlit.io](https://share.streamlit.io) and sign in with GitHub.
3. **New app** ? this repo ? `streamlit_app.py`.
4. In **Secrets**, paste:

```toml
OPENROUTER_API_KEY = "your-key"
OPENROUTER_MODEL = "openai/gpt-4o-mini"
OPENROUTER_APP_NAME = "Data 8 Tutor"
```

5. Deploy. First boot indexes the corpus. The app URL is `https://YOUR-APP.streamlit.app`.

Hosting is free. OpenRouter still charges per question.
