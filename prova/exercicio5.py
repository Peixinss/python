import random

dim_coluna = int(input("Coloque a dimensao da coluna"))
dim_linha = int(input("Coloque a dimensao da linha"))
matriz1 = [[random.randint(1,10) for coluna in range(dim_coluna)]for linha in range (dim_linha)]
matriz2 = [[random.randint(1,10) for coluna in range(dim_coluna)]for linha in range (dim_linha)]

def imprime_matriz(matriz):
    dim_linha = len(matriz)
    dim_coluna = len(matriz[0])
    for linha in range(dim_linha):
        for coluna in range(dim_coluna):
            print(matriz[linha][coluna], end=" ")
        print()