# Game Expert Agent

This repository contains a small RAG-style agent that:

- Indexes local JSON game files under /games folder into a ChromaDB 1.3.x
- Retrieves relevant documents using SentenceTransformer embeddings
- Agent initialized with pre-defined tools to answer questions about the games.

## Quickstart
1. Run the cells inside `Udaplay_01_starter_project.ipynb` notebook to set up the vector database with game data.
2. Run the cells inside `Udaplay_02_starter_project.ipynb` notebook to build and test the AI agent.
