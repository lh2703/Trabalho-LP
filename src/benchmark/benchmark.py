import time
import matplotlib

matplotlib.use('TkAgg')  # Força uso de interface gráfica
import matplotlib.pyplot as plt

from fatorial.fat_iterativo import fat_iterativo
from fatorial.fat_recursivo import fat_recursivo
from fibonacci.fib_iterativo import fib_iterativo
from fibonacci.fib_recursivo import fib_recursivo
from potencia.pot_iterativo import pot_iterativo
from potencia.pot_recursivo import pot_recursivo


escolha = int(input("Escolha um algoritmo:\n1 - Fibonacci\n2 - Fatorial\n3 - Potência\nEscolha: "))

match escolha:
    case 1:
        print("Fibonacci!")
        n = int(input("Digite o valor de n: "))
        valores = list(range(1, n + 1))
        tempos_iterativo = []
        tempos_recursivo = []

        for n in valores:
            inicio_iterativo = time.perf_counter()
            fib_iterativo(n)
            fim_iterativo = time.perf_counter()
            tempos_iterativo.append(fim_iterativo - inicio_iterativo)

            inicio_recursivo = time.perf_counter()
            fib_recursivo(n)
            fim_recursivo = time.perf_counter()
            tempos_recursivo.append(fim_recursivo - inicio_recursivo)

        plt.plot(valores, tempos_iterativo, label='Iterativo')
        plt.plot(valores, tempos_recursivo, label='Recursivo')
        plt.xlabel('Valor de n')
        plt.ylabel('Tempo de execução (s)')
        plt.title('Comparação de tempos: Fibonacci Iterativo vs Recursivo')
        plt.legend()
        plt.grid(True)
        plt.show()

    case 2:
        print("Fatorial!")
        n = int(input("Digite o valor de n: "))

        valores = list(range(1, n+1))
        tempos_iterativo = []
        tempos_recursivo = []

        for n in valores:
            inicio_iterativo = time.perf_counter()
            fat_iterativo(n)
            fim_iterativo = time.perf_counter()
            tempos_iterativo.append(fim_iterativo - inicio_iterativo)

            inicio_recursivo = time.perf_counter()
            fat_recursivo(n)
            fim_recursivo = time.perf_counter()
            tempos_recursivo.append(fim_recursivo - inicio_recursivo)

        plt.plot(valores, tempos_iterativo, label='Iterativo')
        plt.plot(valores, tempos_recursivo, label='Recursivo')
        plt.xlabel('Valor de n')
        plt.ylabel('Tempo de execução (s)')
        plt.title('Comparação de tempos: Fatorial Iterativo vs Recursivo')
        plt.legend()
        plt.grid(True)
        plt.show()
    case 3:
        print("Potência!")
        n = int(input("Digite o expoente: "))
        valores = list(range(1, n + 1))
        tempos_iterativo = []
        tempos_recursivo = []

        for n in valores:
            inicio_iterativo = time.perf_counter()
            pot_iterativo(n)
            fim_iterativo = time.perf_counter()
            tempos_iterativo.append(fim_iterativo - inicio_iterativo)

            inicio_recursivo = time.perf_counter()
            pot_recursivo(n)
            fim_recursivo = time.perf_counter()
            tempos_recursivo.append(fim_recursivo - inicio_recursivo)

        plt.plot(valores, tempos_iterativo, label='Iterativo')
        plt.plot(valores, tempos_recursivo, label='Recursivo')
        plt.xlabel('Valor de n')
        plt.ylabel('Tempo de execução (s)')
        plt.title('Comparação de tempos: Potência Iterativa vs Recursiva')
        plt.legend()
        plt.grid(True)
        plt.show()
    case _:
        print("Escolha inválida.")