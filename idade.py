idade = int (input("Digitige sua idade"))

if idade > 0:
    if idade <= 3:
        print("A idade é de um BEBE")
    elif idade <=12:
        print("A idade é de uma CRIANÇA")
    elif idade <=17:
        print("A idade é de um ADOLESCENTE")
    elif idade >18:
        print("A idade é de um ADULTO")
else:
    print("Erro! A idade não pode ser negativa")


