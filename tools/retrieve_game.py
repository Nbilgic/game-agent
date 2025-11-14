from db import collection
from embeddings import embed

def retrieve_game(query: str, n_results: int = 3):
    query_vector = embed([query])[0]
    results = collection.query(
        query_embeddings=[query_vector],
        n_results=n_results,
        include=['documents','metadatas']
    )
    metadatas = results.get('metadatas', [[]])[0]
    documents = results.get('documents', [[]])[0]
    out = []
    for meta, doc in zip(metadatas, documents):
        out.append({
            'Platform': meta.get('Platform'),
            'Name': meta.get('Name'),
            'YearOfRelease': meta.get('YearOfRelease'),
            'Description': meta.get('Description'),
            'document': doc
        })
    return out
