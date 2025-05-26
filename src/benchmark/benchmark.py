import time
import matplotlib

matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

from fatorial.fat_iterativo import fat_iterativo
from fatorial.fat_recursivo import fat_recursivo

print("Fatorial!")
n = int(input("Digite o valor de n: "))

valores = list(range(1, n + 1))
tempos_iterativo = []
tempos_recursivo = []

for num in valores:
    # tempo iterativo
    inicio_iterativo = time.perf_counter()
    fat_iterativo(num)
    fim_iterativo = time.perf_counter()
    tempos_iterativo.append(fim_iterativo - inicio_iterativo)

    # tempo recursivo
    inicio_recursivo = time.perf_counter()
    fat_recursivo(num)
    fim_recursivo = time.perf_counter()
    tempos_recursivo.append(fim_recursivo - inicio_recursivo)

#grafico
plt.plot(valores, tempos_iterativo, label='Iterativo')
plt.plot(valores, tempos_recursivo, label='Recursivo')
plt.xlabel('Valor de n')
plt.ylabel('Tempo de execução (s)')
plt.title('Comparação de tempos: Fatorial Iterativo vs Recursivo')
plt.legend()
plt.grid(True)
plt.show()

