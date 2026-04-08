def init():
    return {
        "code": """def sum_list(lst):
    s = 0
    for i in range(len(lst)):
        s += lst[i]
    return s""",
        "tests": [
            "assert sum_list([1,2,3])==6",
            "assert sum_list([])==0"
        ]
    }