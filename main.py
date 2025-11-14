from dotenv import load_dotenv
from agent import run_agent

load_dotenv()

if __name__ == '__main__':
    while True:
        q = input('Ask a question about video games (or type exit): ').strip()
        if q.lower() in ('exit','quit'):
            break
        out = run_agent(q)
        print('\n=== RESULT ===')
        print('Source:', out['source'])
        print('Explanation:', out['explanation'])
        print('Data:', out['data'])
        print('\n')
