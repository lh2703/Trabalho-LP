def fib_iterativo(n):
    a = 0
    b = 1
    cont = 2

    while cont < n:
        temp = a + b
        a = b
        b = temp
        cont +=1

    return b

