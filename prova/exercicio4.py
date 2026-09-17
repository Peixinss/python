def addLista(num):
    lista.append(num)
    return lista

lista= []

while True:
    carro = input("Coloque o nome do carro")
    print(f"lista: {addLista(carro)}")
    continua = input("Deseja continuar executando? [s,n]: ").lower()
    if (continua == "n") or (continua == "não") or (continua == "nao"):
        break