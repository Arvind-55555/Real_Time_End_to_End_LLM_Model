import chromadb
from chromadb.config import Settings as ChromaSettings
from chromadb.utils import embedding_functions
from .config import settings
from .embeddings import embed_texts

_client = None
_collection = None

def get_client():
    global _client, _collection
    if _client is None:
        _client = chromadb.Client(chromadb.config.Settings(
            chroma_db_impl="duckdb+parquet",
            persist_directory=settings.CHROMA_DIR
        ))
    return _client

def get_collection(name="documents"):
    global _collection
    if _collection is None:
        client = get_client()
        _collection = client.get_or_create_collection(name=name)
    return _collection

def add_documents(documents, metadatas=None, ids=None):
    """
    documents: list[str]
    metadatas: optional list[dict]
    ids: optional list[str]
    """
    col = get_collection()
    embeddings = embed_texts(documents).tolist()
    col.add(documents=documents, metadatas=metadatas or [{}]*len(documents), ids=ids or None, embeddings=embeddings)
    # persist to disk
    get_client().persist()

def semantic_search(query, k=5):
    col = get_collection()
    # Use Chroma's query-by-text or by embedding
    results = col.query(query_texts=[query], n_results=k)
    # results contain documents, metadatas, distances
    docs = []
    if results and "documents" in results:
        for d, m, dist in zip(results["documents"][0], results["metadatas"][0], results["distances"][0]):
            docs.append({"text": d, "meta": m, "score": float(dist)})
    return docs
