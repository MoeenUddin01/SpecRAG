# SpecRAG 🚀

**SpecRAG** is a modular, production-ready Retrieval-Augmented Generation (RAG) agent pipeline built following **Spec-Driven Development (SDD)** principles. It ingests document datasets, processes and cleans text, builds vector index embeddings, and powers an LLM conversational agent to answer queries over private data accurately.

---

## 🛠️ Tech Stack

- **Language:** Python 3.12+
- **Package Manager:** [`uv`](https://github.com/astral-sh/uv)
- **Orchestration:** LangChain
- **Vector Storage:** FAISS
- **Embeddings:** Jina AI (`jina-embeddings-v2-base-en`)
- **LLM Inference:** Groq (`ChatGroq`)
- **Configuration & Validation:** Pydantic / Pydantic Settings
- **Testing:** Pytest

---

## 📁 Repository Structure

```text
SpecRAG/
├── CLAUDE.md                 # Agent orchestration guidelines
├── PROGRESS.md               # Live project progress & roadmap
├── pyproject.toml            # Dependency definitions via uv
├── .env.example              # Environment secrets template
├── specs/                    # Feature Specifications (Source of Truth)
│   ├── data_ingestion.md     # Document loader & splitter spec
│   ├── preprocessing.md      # Text cleaning & normalization spec
│   ├── vector_storage.md     # FAISS vector store & Jina embedding spec
│   └── agent_tools.md        # RAG agent & tool definitions
├── src/                      # Source Code
│   ├── core/                 # Configuration, logging, and environment settings
│   ├── ingestion/            # Document loaders, preprocessors, and splitters
│   ├── storage/              # Embeddings & FAISS index management
│   ├── agent/                # LLM chains, retrievers, and tools
│   └── main.py               # CLI entry point
└── tests/                    # Unit and integration test suite
```

---

## 📋 Feature Specifications (Source of Truth)

Every feature in SpecRAG is documented in `specs/` prior to implementation:

- 📄 [data_ingestion.md](specs/data_ingestion.md) — Document loading (`.txt`, `.md`, `.pdf`) and text splitting strategy.
- 🧹 [preprocessing.md](specs/preprocessing.md) — Text cleaning, whitespace collapse, and NFKC unicode normalization.
- ⚡ [vector_storage.md](specs/vector_storage.md) — FAISS indexing, similarity search, and Jina embedding integration.
- 🤖 [agent_tools.md](specs/agent_tools.md) — Groq LLM chain and retriever tool definitions.

---

## ⚡ Quickstart & Setup

### 1. Prerequisites
Ensure [`uv`](https://github.com/astral-sh/uv) is installed:
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

### 2. Environment Setup
Clone the repository and install dependencies:
```bash
git clone https://github.com/MoeenUddin01/SpecRAG.git
cd SpecRAG
uv sync
```

### 3. Configure Credentials
Copy `.env.example` to `.env` and add your API keys:
```bash
cp .env.example .env
```
Fill in `.env`:
```ini
GROQ_API_KEY=your_groq_api_key_here
JINA_API_KEY=your_jina_api_key_here
LOG_LEVEL=INFO
ENVIRONMENT=development
```

### 4. Run Test Suite
Run unit tests to verify installation:
```bash
uv run pytest
```

---

## 📊 Project Progress

Track current phase completion and upcoming tasks in [PROGRESS.md](PROGRESS.md).
