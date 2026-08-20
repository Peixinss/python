total = 0
while True:
    produto = float (input("Digite o valor do produto: "))
    total += produto
    print(f"O total parcial é de R${total}")
    continua = input("Deseja inserir mais um produto [s, n]: ".lower())
    if(continua == "n") or (continua == "não") or (continua == "nao"):
        break
print(f"O valor total é de R${total}")

