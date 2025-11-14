import chromadb
import os

from dotenv import load_dotenv

load_dotenv()
CHROMA_PATH = os.getenv('CHROMA_PATH', './chroma_db')

# Persistent client (ChromaDB 1.3.x)
client = chromadb.PersistentClient(path=CHROMA_PATH)

# Create/get collection
collection = client.get_or_create_collection(
    name='games_collection',
    metadata={'hnsw:space': 'cosine'}
)
