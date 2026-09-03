import random

dim_linha = int(input("coloque a quantidades de linha"))
dim_coluna = int(input("coloque a quantidadde de coluna"))
matriz = [[random.randint(1,10) for coluna in range(dim_coluna)]for linha in range (dim_linha)]


for linha in range(dim_linha):
    for coluna in range(dim_coluna):
        print(matriz[linha][coluna], end=" ")
    print()