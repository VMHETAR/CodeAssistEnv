from utils.executor import run_code

def grade(state):
    results = run_code(state["code"], state["tests"])
    if not results:
        return 0.0
    return sum(results) / len(results)
