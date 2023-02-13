import time
from functools import cache

@cache
def fib(n):
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)

start = time.time()
result = fib(35)
end = time.time()

print(result)
print(f'It took {end - start}')