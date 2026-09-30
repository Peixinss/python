import random

def imprime_matriz(matriz):
    dim_linha = len(matriz)
    dim_coluna = len(matriz[0])
    for linha in range(dim_linha):
        for coluna in range(dim_coluna):
            print(matriz[linha][coluna], end=" ")
        print()

dim_coluna = int(input("Coloque a dimensao da matriz"))
dim_linha = dim_coluna
print(" ")
matriz1 = [[random.randint(1,9) for coluna in range(dim_coluna)]for linha in range (dim_linha)]
matriz2 = [[random.randint(1,9) for coluna in range(dim_coluna)]for linha in range (dim_linha)]

print("matriz 1")
imprime_matriz(matriz1)
print(" ")
print("Matriz 2")
imprime_matriz(matriz2)

