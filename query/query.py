import os
from sentence_transformers import SentenceTransformer
from utils.kdb_client import KDBClient
from dotenv import load_dotenv
import openai

load_dotenv()

def generate_answer(query, namespace="default"):
    model = SentenceTransformer("all-MiniLM-L6-v2")
    query_emb = model.encode([query])[0]

    kdb = KDBClient(api_key=os.getenv("KDB_API_KEY"), host=os.getenv("KDB_HOST"))
    results = kdb.query(query_emb.tolist(), namespace=namespace)

    context = "\n".join([r['document'] for r in results])
    prompt = f"Context:\n{context}\n\nQuestion: {query}\nAnswer:"

    openai.api_key = os.getenv("OPENAI_API_KEY")
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )

    return response["choices"][0]["message"]["content"]

if __name__ == "__main__":
    q = "What did Apple report in their recent earnings?"
    print(generate_answer(q))
