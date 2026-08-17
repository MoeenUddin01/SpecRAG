# Feature Specification: Data Ingestion

## Status: Approved

## 1. Overview
The Data Ingestion component is responsible for loading document files from disk (e.g., Markdown, Text, PDF) and splitting them into optimal chunks for embedding generation and retrieval in the SpecRAG pipeline.

---

## 2. Requirements & Scope
- **File Format Support:** Markdown (`.md`), Plain Text (`.txt`), and PDF (`.pdf`).
- **Text Splitting Strategy:** Use LangChain's `RecursiveCharacterTextSplitter` with configurable chunk size and chunk overlap.
- **Metadata Management:** Preserve document source, filename, chunk index, and total chunk count in each chunk's metadata dictionary.
- **Type Safety:** Strict Python type hints across all function signatures.

---

## 3. Architecture & Components

```text
src/ingestion/
├── __init__.py
├── loader.py        # Custom & LangChain document loaders
└── splitter.py      # RecursiveCharacterTextSplitter wrapper
```

### Components:
1. `DocumentLoader` (`src/ingestion/loader.py`):
   - Reads files or directories.
   - Returns a list of `langchain_core.documents.Document` instances.
2. `DocumentSplitter` (`src/ingestion/splitter.py`):
   - Accepts loaded `Document` list (post-preprocessing via `preprocessing.md`).
   - Splits text into chunks with defined `chunk_size` (default: 1000) and `chunk_overlap` (default: 200).

---

## 4. Input & Output Interface

### `DocumentLoader.load_directory(dir_path: str) -> list[Document]`
- **Input:** Directory path containing documents.
- **Output:** List of raw `Document` objects.

### `DocumentSplitter.split_documents(documents: list[Document]) -> list[Document]`
- **Input:** List of `Document` objects.
- **Output:** List of chunked `Document` objects with updated metadata (`chunk_id`, `source`, `total_chunks`).

---

## 5. Phased Implementation Plan ("Tracer Bullets")

- **Phase 1:** Implement `DocumentLoader` supporting `.txt` and `.md` files.
- **Phase 2:** Implement `DocumentSplitter` with `RecursiveCharacterTextSplitter`.
- **Phase 3:** Extend `DocumentLoader` to handle `.pdf` documents using PyPDF loader.
- **Phase 4:** Write unit tests in `tests/test_ingestion.py`.

---

## 6. Verification Plan
- Unit test document loading against mock text files in `tests/test_ingestion.py`.
- Verify chunk length constraint ($len \le chunk\_size$) and chunk overlap presence.


