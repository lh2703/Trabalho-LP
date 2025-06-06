def fib_iterativo(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1

    a = 0
    b = 1
    count = 2

    while count <= n:
        a, b = b, a + b
        count += 1

    return b
