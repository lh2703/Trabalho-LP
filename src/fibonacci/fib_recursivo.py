def fib_recursivo(n)
    if n==0:
        return 0
    if n==1:
        return 1
    return fib_recursivo(n-1) + fib_recursivo(n-2)
