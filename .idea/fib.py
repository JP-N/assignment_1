# fib.py
from functools import lru_cache


# JP Noga
# 1.28.25
# Assignment 1
# Fibonacci - Function to calculate the nth Fibonacci number

@lru_cache
@timer

def fib(n: int) -> int:
    if n <= 1:
        return n
    else:
        return fib(n-1) + fib(n-2)

if __name__ == "__main__":
    t = Timer()
    t.start()
    print(fib(10))
    t.stop()