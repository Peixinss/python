import random
lista = [random.randint(1,100) for tamanho in range(15)]

contador = 0
par = []

for numero in range(15):
    if lista[numero] % 2 == 0:
        contador += 1
        par.append(lista[numero])



print(f"Lista normal: {lista}\n")
print(f"quantidade de pares: {contador}\n")
print(f"Lista par: {par}\n")
