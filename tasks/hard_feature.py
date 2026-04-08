def init():
    return {
        "code": """def calc(a,b,op):
    if op=='+':
        return a+b""",
        "tests": [
            "assert calc(2,3,'+')==5",
            "assert calc(2,3,'*')==6",
            "assert calc(6,3,'/')==2"
        ]
    }