# Data 8 Tutor

A one-page website: intro plus a chatbot that answers Data 8 questions from the course corpus. Student mode only.

GitHub: https://github.com/BenTel86/data8-tutor

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

## Public URL (Streamlit Cloud)

The code is already on GitHub. Finish deploy in one click:

[Deploy to Streamlit Cloud](https://share.streamlit.io/deploy?repository=BenTel86/data8-tutor&branch=main&mainModule=streamlit_app.py)

1. Sign in with GitHub.
2. Confirm repo `BenTel86/data8-tutor`, branch `main`, file `streamlit_app.py`.
3. Before or after deploy, open **Settings ? Secrets** and paste:

```toml
OPENROUTER_API_KEY = "your-key"
OPENROUTER_MODEL = "openai/gpt-4o-mini"
OPENROUTER_APP_NAME = "Data 8 Tutor"
```

4. The public site will be `https://data8-tutor-bentel86.streamlit.app` (or the URL Streamlit shows). First boot indexes the corpus and can take a few minutes.

Hosting is free. OpenRouter still charges per question.
