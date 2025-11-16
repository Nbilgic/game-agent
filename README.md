# Game Expert Agent

This repository contains a small RAG-style agent that:

- Indexes local JSON game files into a ChromaDB 1.3.x collection (manual embeddings)
- Retrieves relevant documents using SentenceTransformer embeddings
- Uses OpenAI to evaluate retrieval quality (LLM judge)
- Falls back to Tavily web search if local docs are insufficient

## Quickstart

# OPTION-1: Using main.py file

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

# OPTION-2: Using Jupyter Notebooks
1. Run the cells inside `Udaplay_01_starter_project.ipynb` notebook to set up the vector database with game data.
2. Run the cells inside `Udaplay_02_starter_project.ipynb` notebook to build and test the AI agent.
