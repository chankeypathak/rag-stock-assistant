# 📈 RAG-Based Stock Assistant (Docker + KDB.AI Cloud)

This project is a **Retrieval-Augmented Generation (RAG) stock assistant**, built using:
- **Python CLI** interface (Dockerized)
- **KDB.AI Cloud** as the vector store (free SaaS tier)
- **HuggingFace embeddings**
- **Real-time stock data sources**: yFinance, RSS, and SEC EDGAR filings

---

## ⚙️ How It Works

1. Ingest stock prices, news, and SEC filings.
2. Embed documents using a SentenceTransformer model.
3. Store embeddings in **KDB.AI Cloud**.
4. Accept a user query via CLI.
5. Embed the query and retrieve top-k similar documents.
6. Generate a natural-language answer using an LLM (local or API).

---

## 🧭 Architecture (Simple)

```mermaid
flowchart TD
  U[User] --> CLI[Python CLI App]

  subgraph Data Sources
    YF[yFinance (Stock Prices)]
    RSS[RSS Feed (News)]
    SEC[SEC Filings (EDGAR 10-K/8-K)]
  end

  subgraph Ingestion
    INGEST[Ingest & Preprocess]
  end

  subgraph Embeddings
    HF[HuggingFace SentenceTransformer]
  end

  subgraph VectorStore
    KDB[KDB.AI Cloud<br/>Vector DB (HFT-friendly)]
  end

  subgraph RAG
    RETRIEVE[Top-k Document Retrieval]
    LLM[Open-source LLM]
  end

  YF --> INGEST
  RSS --> INGEST
  SEC --> INGEST
  INGEST --> HF
  HF --> KDB
  CLI --> HF
  HF --> KDB
  KDB --> RETRIEVE
  RETRIEVE --> CLI
  CLI --> LLM

## 🧱 Extended Architecture (Docker + APIs + CLI)
flowchart TD
  subgraph User Side
    U[User]
    CLI[Python CLI App<br/>(Docker Container)]
    U --> CLI
  end

  subgraph External APIs
    YF[yFinance API]
    RSS[RSS Feeds]
    SEC[EDGAR Filings API]
  end

  subgraph Ingestion Layer
    INGEST[Ingest & Preprocess<br/>(Docker: ingest.py)]
    YF --> INGEST
    RSS --> INGEST
    SEC --> INGEST
  end

  subgraph Embedding Layer
    HF[HuggingFace Embeddings<br/>SentenceTransformer<br/>(Docker: embed.py)]
    INGEST --> HF
    CLI --> HF
  end

  subgraph Vector Store
    KDB[KDB.AI Cloud<br/>(SaaS Vector DB)<br/>HFT-friendly]
    HF --> KDB
    KDB --> CLI
  end

  subgraph RAG & LLM
    RETRIEVE[Retrieve Top-k Docs<br/>(Docker: query.py)]
    LLM[Open-source LLM<br/>e.g. Llama.cpp / Ollama<br/>(Optional Docker)]
    CLI --> RETRIEVE
    RETRIEVE --> LLM
  end

  style CLI fill:#fff2db,stroke:#333,stroke-width:1px
  style HF fill:#d8eafd,stroke:#333,stroke-width:1px
  style KDB fill:#d1ffd6,stroke:#333,stroke-width:1px
  style LLM fill:#e0d3ff,stroke:#333,stroke-width:1px
