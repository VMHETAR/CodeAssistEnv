from typing import List

def run_code(code: str, tests: List[str]) -> List[int]:
    results = []
    namespace = {}
    try:
        exec(code, namespace)
    except Exception:
        return [0] * len(tests)
    
    for test in tests:
        try:
            exec(test, namespace)
            results.append(1)
        except Exception:
            results.append(0)
    return results