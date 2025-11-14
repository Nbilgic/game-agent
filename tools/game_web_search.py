import os

from dotenv import load_dotenv
from tavily import TavilyClient

load_dotenv()

tavily = TavilyClient(api_key=os.getenv('TAVILY_API_KEY'))

def game_web_search(question: str, max_results: int = 3):
    try:
        resp = tavily.search(query=question, include_answer=True, max_results=max_results)
        return {'answer': resp.get('answer'), 'results': resp.get('results')}
    except Exception as e:
        return {'answer': None, 'results': [], 'error': str(e)}
