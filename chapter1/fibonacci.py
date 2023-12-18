from typing import Dict
from functools import lru_cache


def fibonnaci(n: int) -> int:
    if n < 2: return n
    return fibonnaci(n - 1) + fibonnaci(n - 2)




def fib2(n: int) -> int:
    if n < 2:  # base case
        return n
    return fib2(n - 2) + fib2(n - 1)




memo: Dict[int, int] = {0: 0, 1: 1}  # our base cases

def fib3(n: int) -> int:
    if n not in memo:
        memo[n] = fib3(n - 1) + fib3(n - 2)  # memoization
    return memo[n]




@lru_cache(maxsize=None)
def fib4(n: int) -> int:
    if n < 2:  # base case
        return n
    return fib4(n - 2) + fib4(n - 1) 


if __name__ == "__main__":
    print(fibonnaci(4))