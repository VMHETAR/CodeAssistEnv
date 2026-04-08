from utils.executor import run_code

def grade(state):
    results = run_code(state["code"], state["tests"])
    return sum(results) / len(results)