import os, json
from db import collection
from embeddings import embed

GAMES_DIR = './games'

def index_games():
    ids, docs, metas = [], [], []
    for file in sorted(os.listdir(GAMES_DIR)):
        if not file.endswith('.json'):
            continue
        path = os.path.join(GAMES_DIR, file)
        with open(path, 'r', encoding='utf-8') as fh:
            game = json.load(fh)
        text = f"[{game.get('Platform')}] {game.get('Name')} ({game.get('YearOfRelease')}) - {game.get('Description')}"
        doc_id = os.path.splitext(file)[0]
        ids.append(doc_id)
        docs.append(text)
        metas.append(game)
    if not ids:
        print('No JSON files found in', GAMES_DIR)
        return
    print('Embedding', len(docs), 'documents...')
    vectors = embed(docs)
    print('Adding to ChromaDB...')
    collection.add(ids=ids, embeddings=vectors, documents=docs, metadatas=metas)
    print('Indexed', len(ids), 'documents.')

if __name__ == '__main__':
    index_games()
