def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        # print(b)
        yield b
        a, b = b, a + b
        n = n + 1
    return 'done'


if __name__ == '__main__':
    for i in fib(10):
        print(i)

    g = fib(10)
    while True:
        try:
            x = next(g)
            print(x)
        except StopIteration as e:
            print('stop value is: %s' % e.value)
            break


