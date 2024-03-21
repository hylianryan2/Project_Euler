fib_cache = {1:1, 2:2}

def fib(n):
    if n not in fib_cache:
        fib_cache[n] = fib(n - 1) + fib(n - 2)
    return fib_cache[n]

total = 0
n = 1
while (result := fib(n)) <= 4_000_000:
    if result % 2 == 0:
        total += result
    n += 1

print(total)
