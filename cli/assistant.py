import os
from dotenv import load_dotenv
from openai import OpenAI
import requests

load_dotenv()

KDB_API_KEY = os.getenv("KDB_API_KEY")
KDB_COLLECTION = os.getenv("KDB_COLLECTION")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

client = OpenAI(api_key=OPENAI_API_KEY)

def query_kdb(question):
    url = f"https://api.kdb.ai/v1/query"
    headers = {
        "Authorization": f"Bearer {KDB_API_KEY}",
        "Content-Type": "application/json"
    }
    payload = {
        "collection": KDB_COLLECTION,
        "query": question,
        "topK": 5
    }
    response = requests.post(url, headers=headers, json=payload)
    response.raise_for_status()
    results = response.json()
    contexts = [doc["document"]["text"] for doc in results.get("matches", [])]
    return "\n".join(contexts)

def generate_answer(question, context):
    prompt = f"""You are a stock assistant. Based on the context below, answer the question:
Context:
{context}

Question: {question}
Answer:"""
    chat = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.2
    )
    return chat.choices[0].message.content.strip()

def main():
    print("🔍 Ask me anything about the market:")
    while True:
        try:
            question = input("> ").strip()
            if not question:
                continue
            if question.lower() in ["exit", "quit"]:
                break
            context = query_kdb(question)
            answer = generate_answer(question, context)
            print(f"\n📊 {answer}\n")
        except KeyboardInterrupt:
            break
        except Exception as e:
            print("[ERROR]", e)

if __name__ == "__main__":
    main()
