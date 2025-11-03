from fastapi import FastAPI, HTTPException, Body
from pydantic import BaseModel
from .ingest import ingest_batch
from .retriever import semantic_search
from .generator import generate_answer
from .config import settings

app = FastAPI(title="LLM Production API")


class Doc(BaseModel):
    id: str = None
    text: str
    meta: dict = None

class Query(BaseModel):
    query: str
    k: int = 5
    return_docs: bool = True

@app.post("/ingest")
def ingest(docs: list[Doc] = Body(...)):
    docs_payload = [d.dict() for d in docs]
    return ingest_batch(docs_payload)

@app.post("/query")
def query(payload: Query):
    docs = semantic_search(payload.query, k=payload.k)
    return {"query": payload.query, "results": docs}

@app.post("/answer")
def answer(payload: Query):
    # RAG: retrieve, then craft prompt
    docs = semantic_search(payload.query, k=payload.k)
    context = "\n\n".join([d["text"] for d in docs])
    prompt = f"Use the following context to answer the question succinctly.\n\nContext:\n{context}\n\nQuestion: {payload.query}\nAnswer:"
    gen = generate_answer(prompt)
    return {"answer": gen, "sources": docs}
