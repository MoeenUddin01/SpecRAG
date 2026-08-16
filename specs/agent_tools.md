# Feature Specification: Agent Tools & LLM Orchestration

## Status: Approved

## 1. Overview
The Agent & LLM Orchestration module connects the FAISS retriever with **Groq LLM inference** via LangChain to provide context-aware, precise answers based on the ingested documents.

---

## 2. Requirements & Scope
- **LLM Inference:** Groq API via `ChatGroq` (`llama-3.3-70b-versatile` or `mixtral-8x7b-32768`).
- **Retriever Tool:** Wrap the FAISS similarity search as a LangChain tool/retriever.
- **Context Synthesis:** Construct prompts that enforce ground-truth answering (instructing the model to refrain from hallucinating if context is missing).
- **Secrets Management:** Read `GROQ_API_KEY` strictly from `.env`.

---

## 3. Architecture & Components

```text
src/agent/
├── __init__.py
├── llm.py           # Groq LLM setup and configuration
├── retriever.py     # Retriever tool definition
└── chain.py         # RAG chain / Agent execution chain
```

### Components:
1. `GroqLLM` (`src/agent/llm.py`):
   - Configures `ChatGroq` client with model temperature and API keys.
2. `RetrieverTool` (`src/agent/retriever.py`):
   - Exposes FAISS similarity search as a query tool for the LLM.
3. `RAGChain` (`src/agent/chain.py`):
   - Combines Retriever + Prompt Template + Groq LLM into an executable chain.

---

## 4. Prompt Engineering Rules
- Instruct the model: *"Answer the user query based ONLY on the provided context. If the answer cannot be deduced from context, reply: 'I cannot find relevant information in the provided documents.'"*
- Output response along with source document metadata references (source file, chunk ID).

---

## 5. Phased Implementation Plan ("Tracer Bullets")

- **Phase 1:** Setup `GroqLLM` instance using `ChatGroq`.
- **Phase 2:** Implement `RetrieverTool` wrapping FAISS vector store.
- **Phase 3:** Assemble `RAGChain` and response formatter.
- **Phase 4:** Write integration tests in `tests/test_agent.py` using mocked Groq responses.

---

## 6. Verification Plan
- Unit tests verifying prompt formatting and retriever tool execution.
- End-to-end query verification with sample documents.
