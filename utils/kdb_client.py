import os
from dotenv import load_dotenv
import kdbai_client as kdbai

load_dotenv()

class KDBClient:
    def __init__(self):
        self.endpoint = os.getenv("KDBAI_ENDPOINT")
        self.api_key = os.getenv("KDBAI_API_KEY")
        self.session = kdbai.Session(endpoint=self.endpoint, api_key=self.api_key)
        self.db = self.session.database("default")

        self.table_name = os.getenv("KDBAI_TABLE", "documents")

        # if self.table_name not in self.db.tables:
        #     schema = [
        #         {"name": "id", "type": "str"},
        #         {"name": "document", "type": "str"},
        #         {"name": "embeddings", "type": "float32s"}
        #     ]
        #     index = [
        #         {"name": "vectorIndex", "type": "flat", "column": "embeddings",
        #          "params": {"dims": 384, "metric": "L2"}}
        #     ]
        #     self.db.create_table(self.table_name, schema=schema, indexes=index)

        self.table = self.db.table(self.table_name)

    def insert(self, doc_id, text, embedding):
        row = {
            "id": doc_id,
            "document": text,
            "embeddings": embedding
        }
        self.table.insert([row])

    def query(self, embedding, top_k=3):
        results = self.table.search(vectors={"vectorIndex": [embedding]}, n=top_k)
        return [{"document": r["document"]} for r in results]
