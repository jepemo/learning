from typing import Callable, Dict, List
import inspect

def get_caller_globals():
    return inspect.stack()[2][0].f_globals

def read_data(day: int, parser=int, sep='\n', test=False) -> list:
    filepath = f'data/test{day}.txt' if test else f'data/input{day}.txt'
    sections = open(filepath).read().rstrip().split(sep)
    return [parser(section) for section in sections]

def do(day: int, data: list, answers=[], test=False) -> Dict[int, int]:
    g = get_caller_globals()
    results = []
    for currentPart in [1, 2]:
        fname = f'day{day}_{currentPart}'
        if fname in g:
            result = g[fname](data)
            results.append(result)

    pref = "TEST=" if test else "FINAL="
    if (len(answers) > 0):
        ind = 1
        print(pref)
        for (rez, ans) in zip(results, answers):
            if (rez != ans):
                print(f"\tERR: Part{ind} -> Result: {rez} !=== {ans} :Answer")
            else:
                print(f"\tOKI: Part{ind} -> Result: {rez} ==== {ans} :Answer")
            ind += 1

    else:
        print(pref, "\n\t", results)