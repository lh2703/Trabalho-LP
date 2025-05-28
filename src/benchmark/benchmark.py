import time
import matplotlib
matplotlib.use('tkAgg')  # Força uso de interface gráfica
import matplotlib.pyplot as plt

from fatorial.fat_iterativo import fat_iterativo
from fatorial.fat_recursivo import fat_recursivo
from fibonacci.fib_iterativo import fib_iterativo
from fibonacci.fib_recursivo import fib_recursivo
from potencia.pot_iterativo import pot_iterativo
from potencia.pot_recursivo import pot_recursivo

def plotar_grafico(valores_n, tempos_iterativo, tempos_recursivo, titulo_algoritmo):

    plt.plot(valores_n, tempos_iterativo,'o-', label='Iterativo') #Gráfico Iterativo
    plt.plot(valores_n, tempos_recursivo,'o-', label='Recursivo') #Gráfico Recursivo
    plt.xlabel('Valor de n')
    plt.ylabel('Tempo de execução (s)')
    plt.title(f'Comparação de tempos: {titulo_algoritmo} Iterativo vs Recursivo')   #Titulo do algoritmo usado
    plt.legend()                                                        #Ativa as legendas
    plt.grid(True)                                                      #Grade para melhor visibilidade no gráfico.
    plt.show()                                                          #Exibe o gráfico



escolha = int(input("Escolha um algoritmo:\n1 - Fibonacci\n2 - Fatorial\n3 - Potência\nEscolha: "))

match escolha:
    case 1:
        print("Fibonacci!")
        n = int(input("Digite o valor de n: "))
        while n <= 0:
            n = int(input("Valor não suportado, digite outro: "))

        valores = list(range(1, n + 1))
        tempos_iterativo = []
        tempos_recursivo = []
        titulo_algoritmo = "Fibonacci"

        for i in valores:
            inicio_iterativo = time.perf_counter()
            fib_iterativo(i)
            fim_iterativo = time.perf_counter()
            tempos_iterativo.append(fim_iterativo - inicio_iterativo)

            inicio_recursivo = time.perf_counter()
            fib_recursivo(i)
            fim_recursivo = time.perf_counter()
            tempos_recursivo.append(fim_recursivo - inicio_recursivo)

        plotar_grafico(valores, tempos_iterativo, tempos_recursivo, titulo_algoritmo)

    case 2:
        print("Fatorial!")
        n = int(input("Digite o valor de n: "))
        while n <= 0:
            n = int(input("Valor não suportado, digite outro: "))

        valores = list(range(1, n+1))
        tempos_iterativo = []
        tempos_recursivo = []
        titulo_algoritmo = "Fatorial"

        for i in valores:
            inicio_iterativo = time.perf_counter()
            fat_iterativo(i)
            fim_iterativo = time.perf_counter()
            tempos_iterativo.append(fim_iterativo - inicio_iterativo)

            inicio_recursivo = time.perf_counter()
            fat_recursivo(i)
            fim_recursivo = time.perf_counter()
            tempos_recursivo.append(fim_recursivo - inicio_recursivo)

        plotar_grafico(valores, tempos_iterativo, tempos_recursivo, titulo_algoritmo)

    case 3:
        print("Potência!")
        x = int(input("Digite o valor da base: "))
        n = int(input("Digite o valor do expoente: "))


        valores = list(range(1, n + 1))
        tempos_iterativo = []
        tempos_recursivo = []
        titulo_algoritmo = "Potência"

        for i in valores:
            inicio_iterativo = time.perf_counter()
            pot_iterativo(x, i)
            fim_iterativo = time.perf_counter()
            tempos_iterativo.append(fim_iterativo - inicio_iterativo)

            inicio_recursivo = time.perf_counter()
            pot_recursivo(x, i)
            fim_recursivo = time.perf_counter()
            tempos_recursivo.append(fim_recursivo - inicio_recursivo)

        plotar_grafico(valores, tempos_iterativo, tempos_recursivo, titulo_algoritmo)

    case _:
        print("Escolha inválida.")
