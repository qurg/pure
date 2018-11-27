from functools import reduce
from fib import fib

n, a, b = 0, 0, 1


def fib_next(m, n):
    return m + n


if __name__ == '__main__':
    result = reduce(fib_next, fib(10))
    print(result)
