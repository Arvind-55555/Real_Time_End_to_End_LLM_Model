from .retriever import add_documents
from .config import settings
from typing import List
import json

def ingest_batch(docs: List[dict]):
    """
    Accepts list of {"id": str, "text": str, "meta": {...}}
    """
    texts = [d["text"] for d in docs]
    metadatas = [d.get("meta", {}) for d in docs]
    ids = [d.get("id") for d in docs]
    add_documents(documents=texts, metadatas=metadatas, ids=ids)
    return {"status": "ok", "count": len(docs)}
