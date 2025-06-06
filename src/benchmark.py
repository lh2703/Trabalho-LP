import time
import matplotlib
import matplotlib.pyplot as plt
matplotlib.use('tkAgg')  # Força uso de interface gráfica
from tqdm import tqdm
import tracemalloc

from fatorial.fat_iterativo import fat_iterativo
from fatorial.fat_recursivo import fat_recursivo
from fibonacci.fib_iterativo import fib_iterativo
from fibonacci.fib_recursivo import fib_recursivo
from mdc.mdc_iterativo import mdc_iterativo
from mdc.mdc_recursivo import mdc_recursivo

def plotar_tempo_e_memoria(valores_n, tempos_iterativo, tempos_recursivo, memorias_iterativo, memorias_recursivo, titulo_algoritmo):
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8))

    # grafico do tempo de execução
    ax1.plot(valores_n, tempos_iterativo, '-o', label='Iterativo')
    ax1.plot(valores_n, tempos_recursivo, '-o', label='Recursivo')
    ax1.set_title(f'{titulo_algoritmo} - Tempo de Execução')
    ax1.set_xlabel('Valor de n')
    ax1.set_ylabel('Tempo (s)')
    ax1.legend()
    ax1.grid(True)

    # grafico de memoria
    ax2.plot(valores_n, memorias_iterativo, '-o', label='Iterativo')
    ax2.plot(valores_n, memorias_recursivo, '-o', label='Recursivo')
    ax2.set_title(f'{titulo_algoritmo} - Uso de Memória')
    ax2.set_xlabel('Valor de n')
    ax2.set_ylabel('Memória Pico (KB)')
    ax2.legend()
    ax2.grid(True)

    plt.show()

def medir_tempo_memoria(funcao, *args):
    tracemalloc.start()
    inicio = time.perf_counter()

    funcao(*args) #executa a função com os argumentos

    fim = time.perf_counter()
    memoria_atual, memoria_pico = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    tempo_execucao = fim - inicio
    memoria_kb = memoria_pico/1024 #converte pra KB

    return tempo_execucao, memoria_kb

def comparar_algoritmos(tempos_it, tempos_rec, mem_it, mem_rec, titulo_algoritmo):
    media_tempo_it = sum(tempos_it) / len(tempos_it)
    media_tempo_rec = sum(tempos_rec) / len(tempos_rec)
    media_mem_it = sum(mem_it) / len(mem_it)
    media_mem_rec = sum(mem_rec) / len(mem_rec)

    print("\n--- Comparação de Desempenho ---")
    print(f"{titulo_algoritmo}")
    print(f"Tempo médio - Iterativo: {media_tempo_it:.6e} s")
    print(f"Tempo médio - Recursivo: {media_tempo_rec:.6e} s")
    print(f"Memória média - Iterativo: {media_mem_it:.6f} KB")
    print(f"Memória média - Recursivo: {media_mem_rec:.6f} KB")

    pontuacao_it = 0
    pontuacao_rec = 0

    if media_tempo_it < media_tempo_rec:
        pontuacao_it += 1
    else:
        pontuacao_rec += 1

    if media_mem_it < media_mem_rec:
        pontuacao_it += 1
    else:
        pontuacao_rec += 1

    if pontuacao_it > pontuacao_rec:
        print("🟢 A implementação **ITERATIVA** apresenta melhor desempenho geral.")
    elif pontuacao_rec > pontuacao_it:
        print("🟢 A implementação **RECURSIVA** apresenta melhor desempenho geral.")
    else:
        print("🟢 As implementações possuem desempenho equivalente.")


def executar_fibonacci():
    print("Fibonacci!")
    n = int(input("Digite o valor de n: "))
    while n <= 0:
        n = int(input("Valor não suportado, digite outro: "))

    valores = list(range(1, n + 1))
    tempos_iterativo = []
    memoria_iterativo = []
    tempos_recursivo = []
    memoria_recursivo = []
    titulo_algoritmo = "Fibonacci"

    for i in tqdm(valores):
        t_it, m_it = medir_tempo_memoria(fib_iterativo, i)
        t_rec, m_rec = medir_tempo_memoria(fib_recursivo, i)

        tempos_iterativo.append(t_it)
        memoria_iterativo.append(m_it)
        tempos_recursivo.append(t_rec)
        memoria_recursivo.append(m_rec)

    plotar_tempo_e_memoria(valores, tempos_iterativo, tempos_recursivo, memoria_iterativo, memoria_recursivo, titulo_algoritmo)
    comparar_algoritmos(tempos_iterativo, tempos_recursivo, memoria_iterativo, memoria_recursivo, titulo_algoritmo)

def executar_fatorial():
    print("Fatorial!")
    n = int(input("Digite o valor de n: "))
    while n <= 0:
        n = int(input("Valor não suportado, digite outro: "))

    valores = list(range(1, n + 1))
    tempos_iterativo = []
    memoria_iterativo = []
    tempos_recursivo = []
    memoria_recursivo = []
    titulo_algoritmo = "Fatorial"

    for i in tqdm(valores):
        t_it, m_it = medir_tempo_memoria(fat_iterativo, i)
        t_rec, m_rec = medir_tempo_memoria(fat_recursivo, i)

        tempos_iterativo.append(t_it)
        memoria_iterativo.append(m_it)
        tempos_recursivo.append(t_rec)
        memoria_recursivo.append(m_rec)

    plotar_tempo_e_memoria(valores, tempos_iterativo, tempos_recursivo, memoria_iterativo, memoria_recursivo, titulo_algoritmo)
    comparar_algoritmos(tempos_iterativo, tempos_recursivo, memoria_iterativo, memoria_recursivo, titulo_algoritmo)

def executar_mdc():
    print("MDC - Varia primeiro número, segundo fixo")
    b = int(input("Digite o segundo número (fixo): "))
    while b <= 0:
        b = int(input("Valor inválido, digite outro: "))

    n = int(input("Digite o valor máximo para o primeiro número (1 até n): "))
    while n <= 0:
        n = int(input("Valor inválido, digite outro: "))

    valores = list(range(1, n + 1))
    tempos_iterativo = []
    memoria_iterativo = []
    tempos_recursivo = []
    memoria_recursivo = []
    titulo_algoritmo = f"MDC com segundo número fixo = {b}"

    for a in tqdm(valores):
        t_it, m_it = medir_tempo_memoria(mdc_iterativo, a, b)
        t_rec, m_rec = medir_tempo_memoria(mdc_recursivo, a, b)

        tempos_iterativo.append(t_it)
        memoria_iterativo.append(m_it)
        tempos_recursivo.append(t_rec)
        memoria_recursivo.append(m_rec)

    plotar_tempo_e_memoria(valores, tempos_iterativo, tempos_recursivo, memoria_iterativo, memoria_recursivo, titulo_algoritmo)
    comparar_algoritmos(tempos_iterativo, tempos_recursivo, memoria_iterativo, memoria_recursivo, titulo_algoritmo)

def main():
    while True:
        escolha = input("\nEscolha um algoritmo:\n1 - Fibonacci\n2 - Fatorial\n3 - MDC\n0 - Sair\nEscolha: ")
        if escolha == "1":
            executar_fibonacci()
        elif escolha == "2":
            executar_fatorial()
        elif escolha == "3":
            executar_mdc()
        elif escolha == "0":
            print("Saindo...")
            break
        else:
            print("Escolha inválida")


if __name__ == "__main__":
    main()