from sentence_transformers import SentenceTransformer

# Use a small, fast model for local embeddings
embedder = SentenceTransformer('all-MiniLM-L6-v2')

def embed(texts: list[str]):
    """Return list of vectors (lists of floats)."""
    vectors = embedder.encode(texts, convert_to_numpy=True)
    return vectors.tolist()
