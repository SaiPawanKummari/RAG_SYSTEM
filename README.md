# RAG SYSTEM FROM SCRATCH

A modular Retrieval Augmented Generation(RAG) using:
- FastEmbed
- FAISS
- LangChain
- Ollama
- Python

This project demonstrated how modern RAG pipelines work internally, including:
- document ingestion
- chunking
- embeddings
- vector indexing
- retrieval
- prompt grounding
- local LLM inference

---

# Architecture

```text
Documents
    ↓
Document Loader
    ↓
Chunking
    ↓
Embedding Generation (FastEmbed)
    ↓
FAISS Vector Store
    ↓
Retriever
    ↓
Prompt Builder
    ↓
LLM (Ollama)
    ↓
Grounded Response
```

---

# Project Structure

```text
rag_project/
│
├── data/
│   └── sample.pdf
│
├── ingestion/
│   ├── loader.py
│   ├── chunker.py
│   └── embedder.py
│
├── vectorstore/
│   └── faiss_store.py
│
├── retrieval/
│   └── retriever.py
│
├── generation/
│   ├── prompt_builder.py
│   └── llm.py
│
├── main.py
└── README.md
```

---

# Technologies Used

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| LangChain | Document loading and chunking |
| FastEmbed | Embedding generation |
| FAISS | Vector similarity search |
| Ollama | Local LLM inference |
| TinyLlama |

---

# How Retrieval Works

1. User query is converted into embeddings
2. FAISS performs semantic similarity search
3. Top relevant chunks are retrieved
4. Retrieved context is injected into the prompt
5. LLM generates grounded response

---

---

# Setup Instructions

## Clone Repository

```bash
git clone https://github.com/SaiPawanKummari/RAG_SYSTEM.git
```

---

## Create Virtual Environment

```bash
python -m venv venv
```

Activate:

```bash
venv\Scripts\activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Install Ollama

Download Ollama:

https://ollama.com/download

---

## Pull Lightweight Model

```bash
ollama pull tinyllama
```

---

## Run Project

```bash
python main.py
```

---

# Future Improvements

- Hybrid Retrieval (BM25 + Vector Search)
- Re-ranking
- Persistent Vector Database
- Conversational Memory
- Streamlit UI
- API Deployment
- Multi-document Retrieval
