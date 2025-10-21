# 🧠 Proyecto: AI Knowledge Assistant (Agente RAG)

Un asistente inteligente capaz de responder preguntas sobre una base de conocimiento propia (por ejemplo, documentos técnicos, PDFs de producto o una base SQL).

## 🎯 Objetivo

Construir un agente LLM con RAG (Retrieval-Augmented Generation) que:

- Incruste (embed) documentos o textos.
- Busque información relevante con similitud semántica.
- Responda usando un LLM con contexto.
- Exponga una API (FastAPI) y una interfaz (Streamlit).
- Evalúe la calidad de respuestas (cosine similarity).

## 🧩 Stack

- LangChain o LangGraph (core de orquestación)
- ChromaDB (vector store)
- OpenAI o HuggingFace (embeddings y LLM)
- FastAPI (backend)
- Streamlit o Gradio (frontend)
- Pytest (tests)
- Docker (deployment opcional)

## 📂 Estructura del proyecto
```
ai-knowledge-assistant/
├── src/
│   ├── main.py                # FastAPI app
│   ├── rag_pipeline.py        # RAG logic
│   ├── utils/
│   │   ├── loader.py          # Document/data loading
│   │   ├── evaluator.py       # Response similarity metric
│   │   └── config.py          # API keys/settings management
│
├── app/
│   └── ui.py                  # Streamlit/Gradio interface
│
├── tests/
│   └── test_agent.py          # Basic unit tests
│
├── requirements.txt
├── README.md
└── .env.example
```
