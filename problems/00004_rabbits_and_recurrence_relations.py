import sys

def fib(k):
    curr, _next = 1, 1
    while True:
        yield curr
        curr, _next = _next, _next + (k * curr)


if len(sys.argv) > 1:
    n, k = int(sys.argv[1]), int(sys.argv[2])
else:
    n, k = open(f"{__file__.split('.')[0]}.input.txt", "r").read().split()
    n, k = int(n), int(k)

for i, j in enumerate(fib(k), 1):
    if i == n:
        print(j)
        break

