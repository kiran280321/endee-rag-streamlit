import os
from sentence_transformers import SentenceTransformer
from endee_client import EndeeClient

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_PATH = os.path.join(BASE_DIR, "data", "sample_docs")

model = SentenceTransformer("all-MiniLM-L6-v2")
db = EndeeClient()

def ingest():
    for file in os.listdir(DATA_PATH):
        with open(os.path.join(DATA_PATH, file), "r", encoding="utf-8") as f:
            text = f.read()

        for chunk in text.split("\n"):
            if chunk.strip():
                embedding = model.encode(chunk).tolist()
                db.add(embedding, {"text": chunk})

    return db
