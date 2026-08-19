somaTotal = 0
for repeticao in range(1,6):
    produto = float(input(f"coloque o valor do produto {repeticao}"))
    somaTotal += produto
print(f"O valor total deu {somaTotal}")
