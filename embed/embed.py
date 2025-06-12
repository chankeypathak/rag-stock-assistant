import os
from sentence_transformers import SentenceTransformer
from utils.kdb_client import KDBClient
from dotenv import load_dotenv

load_dotenv()

def embed_and_store(docs, namespace="default"):
    model = SentenceTransformer("all-MiniLM-L6-v2")
    embeddings = model.encode([doc["content"] for doc in docs])

    kdb = KDBClient(api_key=os.getenv("KDB_API_KEY"), host=os.getenv("KDB_HOST"))
    for doc, emb in zip(docs, embeddings):
        kdb.insert(doc["id"], doc["content"], emb.tolist(), namespace=namespace)

    print(f"[INFO] {len(docs)} documents embedded and stored in KDB.AI")

# Example usage (not for prod)
if __name__ == "__main__":
    dummy_docs = [{"id": "test1", "content": "Apple released earnings this quarter..."}]
    embed_and_store(dummy_docs)
