def fat_recursivo(n):
    if n == 0 or n == 1:
        return 1
    return n * fat_recursivo(n-1)
