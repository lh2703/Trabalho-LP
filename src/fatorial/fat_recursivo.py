def fat_recursivo(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return n * fat_recursivo(n-1)
