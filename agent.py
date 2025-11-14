import json
from tools.retrieve_game import retrieve_game
from tools.evaluate_retrieval import evaluate_retrieval
from tools.game_web_search import game_web_search

from openai import OpenAI
import os

client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'), base_url=os.getenv('OPENAI_BASE_URL'))

def run_agent(question: str):
    print('🔎 Retrieving from local DB...')
    local_results = retrieve_game(question)

    print('🧠 Evaluating retrieval quality...')
    evaluation = evaluate_retrieval(question, local_results)

    if evaluation.useful:
        return {
            'source': 'local',
            'data': local_results,
            'explanation': evaluation.description
        }

    print('🌐 Local data insufficient → using web search...')
    web = game_web_search(question)

    # Ask LLM to synthesize the web output + local results
    prompt = f"""The local database did not contain enough information.

Question: {question}

Local results: {json.dumps(local_results, indent=2)}

Web search results: {json.dumps(web, indent=2)}

Provide a concise, accurate answer to the user."""

    resp = client.chat.completions.create(
        model=os.getenv('ANSWER_MODEL', 'gpt-3.5-turbo'),
        messages=[{'role': 'user', 'content': prompt}],
        temperature=0.7
    )
    final = resp.choices[0].message.content
    return {'source': 'web', 'data': final, 'explanation': evaluation.description}
