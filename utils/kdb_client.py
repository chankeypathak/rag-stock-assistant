import requests

class KDBClient:
    def __init__(self, api_key, host):
        self.api_key = api_key
        self.host = host.rstrip("/")

    def insert(self, doc_id, text, embedding, namespace="default"):
        url = f"{self.host}/v1/upsert"
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
        payload = {
            "namespace": namespace,
            "documents": [{
                "id": doc_id,
                "embedding": embedding,
                "document": text
            }]
        }
        r = requests.post(url, json=payload, headers=headers)
        if r.status_code != 200:
            print(f"[ERROR] KDB insert failed: {r.text}")

    def query(self, embedding, namespace="default", top_k=3):
        url = f"{self.host}/v1/query"
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
        payload = {
            "namespace": namespace,
            "embedding": embedding,
            "topK": top_k
        }
        r = requests.post(url, json=payload, headers=headers)
        if r.status_code != 200:
            print(f"[ERROR] KDB query failed: {r.text}")
            return []
        return r.json().get("matches", [])
