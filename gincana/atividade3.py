import random

def imprime_matriz(matriz):
    dim_linha = len(matriz)
    dim_coluna = len(matriz[0])
    for linha in range(dim_linha):
        for coluna in range(dim_coluna):
            print(matriz[linha][coluna], end=" ")
        print()

matriz = [[random.randint(1,10) for coluna in range(5)]for linha in range (5)]

somaDiagonal = 0

somaDiagonal = matriz[0][0] + matriz [1][1] + matriz[2][2] + matriz [3][3] + matriz [4][4]

imprime_matriz(matriz)
print(f"Soma da diagonal {somaDiagonal}")



