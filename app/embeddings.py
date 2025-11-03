from sentence_transformers import SentenceTransformer
from .config import settings

_embedder = None

def get_embedder():
    global _embedder
    if _embedder is None:
        _embedder = SentenceTransformer(settings.EMBED_MODEL, device=settings.DEVICE)
    return _embedder

def embed_texts(texts):
    model = get_embedder()
    embs = model.encode(texts, convert_to_numpy=True, show_progress_bar=False)
    return embs
