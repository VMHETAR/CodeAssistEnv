def init():
    return {
        "code": """def add(a, b):
    return a - b""",
        "tests": [
            "assert add(2,3)==5",
            "assert add(-1,1)==0"
        ]
    }