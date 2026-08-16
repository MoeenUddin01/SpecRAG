# RAG Agent Pipeline orchestration

## Project Context
This repository contains a modular Retrieval-Augmented Generation (RAG) system. The pipeline ingests documents, processes them into vector embeddings, and provides a conversational interface powered by large language models to query private data.

## Tech Stack
- **Language:** Python
- **Package Manager:** `uv`
- **Orchestration:** LangChain
- **Vector Store:** FAISS
- **Embeddings:** Jina
- **LLM Inference:** Groq

## Modular Architecture
```text
.
├── CLAUDE.md             # AI orchestration instructions
├── specs/                # Feature specifications (Source of Truth)
│   ├── data_ingestion.md
│   ├── vector_storage.md
│   └── agent_tools.md
├── src/
│   ├── core/             # Configuration, logging, and environment management
│   ├── ingestion/        # Document loaders, splitters (RecursiveCharacterTextSplitter)
│   ├── storage/          # Embedding generation and FAISS index management
│   └── agent/            # LLM chains, retrievers, and tool definitions
├── tests/                # Unit and integration tests
├── .env                  # Secrets (Groq, Jina API keys)
└── pyproject.toml        # Dependency management via uv
```

## Build & Run Commands
- **Environment Setup:** `uv venv`
- **Activate:** `source .venv/bin/activate`
- **Install Dependencies:** `uv pip install -r pyproject.toml`
- **Run Pipeline:** `uv run python -m src.main`
- **Formatting:** `uv run ruff format .`

---

# Spec-Driven Development Workflow

## Core Principle

This project uses Spec-Driven Development (SDD).

Do NOT immediately start writing code when given a new feature request.

The workflow is:

1. Understand the request.
2. Inspect the existing codebase and project architecture.
3. Inspect existing specifications in `specs/`.
4. Create or update the appropriate specification.
5. Break the feature into small, independently shippable phases ("tracer bullets").
6. Review the specification before implementation.
7. Implement one approved phase at a time.
8. Test and verify the implementation.
9. Reconcile the specification with the actual implementation.
10. Only then move to the next phase.

The specification is the source of truth for intended behavior.

---

# 1. Before Starting Any Feature

When a new feature or change is requested:

- Do NOT immediately modify code.
- First inspect the relevant parts of the repository.
- Read `CLAUDE.md`.
- Inspect relevant files under `specs/`.
- Inspect existing architecture, models, APIs, services, frontend components, and tests.
- Identify existing patterns that should be reused.
- Identify dependencies and possible conflicts.

Do not reinvent existing functionality without a reason.

---

# 2. Specifications

All feature specifications must live under:

`specs/`

Use a clear and consistent naming convention.

Example:

```text
specs/
├── data_ingestion.md
├── embeddings.md
├── vector_search.md
└── agent_chain.md
```

## 3. Code Style & Conventions
- Use Python type hints strictly for all function signatures.
- Build modular components to support phase-by-phase implementation and testing.
- Isolate API keys and secrets in the `.env` file; never hardcode them.
