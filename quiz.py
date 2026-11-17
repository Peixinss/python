while True:
    pontos = 0
    print(" 1) Qual a capital da Franca ? \n a) Paris \n b) Brasilía \n c) Nova York \n d) Diadema\n")
    resposta1 = input(": ")
    if resposta1 == "a":
        print("Resposta correta!\n")
        pontos +=  1
        print(f"Você tem: {pontos} pontos\n")
    else:
        print("Resposta Errada!\n")
    print(" 2) Qual é a cor do céu ? \n a) Branco \n b) Rosa \n c) Vermelho \n d) Azul\n")
    resposta2 = input(": ")
    if resposta2 == "d":
        print("Resposta correta!\n")
        pontos +=  1
        print(f"Você tem: {pontos} pontos\n")
    else:
        print("Resposta Errada!\n")
    print(" 3) Qual país fica localizado ao mais sul da america do sul ? \n a)Peru \n b) Brasil \n c) Argentina \n d) Russia\n")
    resposta3 = input(": ")
    if resposta3 == "c":
        print("Resposta correta!\n")
        pontos +=  1
        print(f"Você tem: {pontos} pontos\n")
    else:
        print("Resposta Errada!\n")
    print(" 4) Quantos chifres tem um rinoceronte ? \n a)1 \n b) 2 \n c) 3 \n d) 4\n")
    resposta4 = input(": ")
    if resposta4 == "b":
        print("Resposta correta!\n")
        pontos +=  1
        print(f"Você tem: {pontos} pontos\n")
    else:
        print("Resposta Errada!\n")

    print("Dejesa tentar denovo ? (s/n)")
    tentardenovo = input(": ").lower
    if tentardenovo == "n":
        break
