import random 

def imprime_matriz(matriz):
    dim_linha = len(matriz)
    dim_coluna = len(matriz[0])
    for linha in range(dim_linha):
        for coluna in range(dim_coluna):
            print(matriz[linha][coluna], end=" ")
        print()
matriz = [[random.randint(1,10) for coluna in range(3)]for linha in range (3)]
imprime_matriz(matriz)

opcao = int(input("\n Digite 0, 1 ou 2 para somar linha especifica: "))
soma = 0
match opcao:
    case 0:
        linha = matriz[0]
        for elemtento in linha:
            soma += elemtento
        print(f"A soma da linha 0 é: {soma}")
    case 1:
        linha = matriz[1]
        for elemtento in linha:
            soma += elemtento
        print(f"A soma da linha 0 é: {soma}")
    case 2:
        linha = matriz[2]
        for elemtento in linha:
            soma += elemtento
        print(f"A soma da linha 0 é: {soma}")
    case _:
        print("Opcao invalida. Digite 0, 1 ou 2")