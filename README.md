# Game Expert Agent

This repository contains a small RAG-style agent that:

- Indexes local JSON game files into a ChromaDB 1.3.x collection (manual embeddings)
- Retrieves relevant documents using SentenceTransformer embeddings
- Uses OpenAI to evaluate retrieval quality (LLM judge)
- Falls back to Tavily web search if local docs are insufficient

## Quickstart

1. Create a Python virtual environment and activate it.
2. Install dependencies:
```bash
pip install -r requirements.txt
```
3. Index the games (run once):
```bash
python index_games.py
```
4. Run the agent:
```bash
python main.py
```
