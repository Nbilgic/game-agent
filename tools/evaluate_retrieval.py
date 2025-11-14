import json

from dotenv import load_dotenv
from pydantic import BaseModel
from openai import OpenAI
import os

load_dotenv()

client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'), base_url=os.getenv('OPENAI_BASE_URL'))

class EvaluationReport(BaseModel):
    useful: bool
    description: str

def evaluate_retrieval(question: str, retrieved_docs: list[dict]):
    prompt = f"""Your task is to decide whether the retrieved documents are sufficient to answer the question.

Question:
{question}

Retrieved Documents:
{json.dumps(retrieved_docs, indent=2)}

Explain whether the documents contain enough information. Then return valid JSON exactly like:
{{"useful": true, "description": "..."}}
"""

    resp = client.chat.completions.create(
        model=os.getenv('EVAL_MODEL', 'gpt-3.5-turbo'),
        messages=[{'role': 'user', 'content': prompt}],
        temperature=0
    )
    content = resp.choices[0].message.content
    # parse JSON
    try:
        parsed = json.loads(content)
        return EvaluationReport.model_validate(parsed)
    except Exception:
        # fallback: treat as not useful and include raw output
        return EvaluationReport(useful=False, description='Could not parse judge output: ' + content)
