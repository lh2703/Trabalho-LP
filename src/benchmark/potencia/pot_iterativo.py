def pot_iterativo(x,n):
    resultado = 1
    contador = 0
    while contador < n:
        resultado *= x
        contador += 1
    return resultado