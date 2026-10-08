import random

def imprime_matriz(matriz):
    dim_linha = len(matriz)
    dim_coluna = len(matriz[0])
    for linha in range(dim_linha):
        for coluna in range(dim_coluna):
            print(matriz[linha][coluna], end=" ")
        print()

matriz = [[random.randint(1,10) for coluna in range(3)]for linha in range (3)]

soma = 0

for i in range (3):
    contador = matriz[i]
    for elemento in contador:
        soma += elemento

imprime_matriz(matriz)

print(f"A soma da matriz é de: {soma} ")
