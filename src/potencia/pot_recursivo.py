def pot_recursivo(n):
    if n == 0:
        return 1
    return 2 * pot_recursivo(n-1)