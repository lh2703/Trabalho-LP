def mdc_recursivo(a, b):
    if b == 0:
        return a
    return mdc_recursivo(b, a % b)