# 📈 RAG-Based Stock Assistant

This project is a **Retrieval-Augmented Generation (RAG) stock assistant**, built using:
- **Python CLI** interface (Dockerized)
- **KDB.AI Cloud** as the vector store (free SaaS tier)
- **HuggingFace embeddings**
- **Real-time stock data sources**: yFinance, RSS, and SEC EDGAR filings


This project implements a Retrieval-Augmented Generation (RAG) pipeline tailored for financial use cases. It ingests real-time stock prices (via yFinance), market-moving news (via RSS), and company disclosures (via SEC EDGAR).

The documents are embedded using a HuggingFace transformer and stored in KDB.AI Cloud, a high-performance vector database. Queries from users are embedded, top-k relevant documents are retrieved, and responses are generated via an LLM.

Designed for easy replication with Docker, this assistant can support decision-making for investors, researchers, or algorithmic trading environments.

---

## Process

1. Ingest stock prices, news, and SEC filings.
2. Embed documents using a SentenceTransformer model.
3. Store embeddings in **KDB.AI Cloud**.
4. Accept a user query via CLI.
5. Embed the query and retrieve top-k similar documents.
6. Generate a natural-language answer using an LLM (local or API).

---

## Components Overview
| Component            | Description                                               |
| -------------------- | --------------------------------------------------------- |
| `ingest.py`          | Fetch & preprocess news, stock data, filings              |
| `embed.py`           | Generate embeddings using HuggingFace                     |
| `query.py`           | Query KDB.AI and trigger LLM-based response               |
| `docker-compose.yml` | Run CLI + processing modules in containers                |
| `KDB.AI`             | Vector DB (SaaS) used for storing and querying embeddings |
| `CLI Interface`      | User interacts with RAG system via terminal               |

## TODO
- Add Streamlit UI
- Add alerts for stock anomalies
- Key management in Docker