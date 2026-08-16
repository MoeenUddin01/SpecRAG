# Feature Specification: Vector Storage & Embeddings

## Status: Approved

## 1. Overview
The Vector Storage component is responsible for transforming chunked text documents into dense vector representations using the **Jina AI Embeddings API** and indexing them into a **FAISS** vector store for efficient similarity search.

---

## 2. Requirements & Scope
- **Embedding Generation:** Use Jina AI API (`jina-embeddings-v2-base-en`).
- **Vector Index:** Use FAISS (`faiss-cpu`) for fast in-memory similarity search.
- **Persistence:** Save the FAISS index and document store to local disk (`data/faiss_index`) and support loading existing indexes.
- **Querying:** Perform top-$k$ similarity searches given a query string.
- **Secrets Management:** Read `JINA_API_KEY` strictly from `.env`.

---

## 3. Architecture & Components

```text
src/storage/
├── __init__.py
├── embeddings.py    # Jina Embeddings wrapper
└── faiss_store.py   # FAISS store initialization, save/load, and retrieval
```

### Components:
1. `JinaEmbeddingService` (`src/storage/embeddings.py`):
   - Initializes Jina embedding client using `JINA_API_KEY`.
   - Generates vector embeddings for query strings and document lists.
2. `FAISSVectorStore` (`src/storage/faiss_store.py`):
   - `build_from_documents(documents: list[Document]) -> FAISS`
   - `save_local(folder_path: str) -> None`
   - `load_local(folder_path: str) -> FAISS`
   - `similarity_search(query: str, k: int = 4) -> list[Document]`

---

## 4. Phased Implementation Plan ("Tracer Bullets")

- **Phase 1:** Implement `JinaEmbeddingService` with environment variable key retrieval.
- **Phase 2:** Implement `FAISSVectorStore` creation and similarity search.
- **Phase 3:** Add local persistence (`save_local` and `load_local`).
- **Phase 4:** Write integration tests in `tests/test_storage.py` (with mocked Jina embeddings).

---

## 5. Verification Plan
- Unit tests validating index creation, document insertion, and local persistence load/save cycles.
- Mock Jina API calls to verify vector retrieval logic without burning API credits during test runs.
