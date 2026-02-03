from sentence_transformers import SentenceTransformer
from ingest import ingest

model = SentenceTransformer("all-MiniLM-L6-v2")
db = ingest()

def semantic_search(query, top_k=3):
    query_vec = model.encode(query).tolist()
    results = db.search(query_vec, top_k)
    return [item[1]["text"] for item in results]
