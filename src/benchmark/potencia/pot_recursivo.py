def pot_recursivo(x,n):
    if n == 0:
        return 1
    return x * pot_recursivo(n-1,x)