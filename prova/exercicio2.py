escolha = int(input("Escolha o dia da semana"))

match escolha:
    case  escolha if escolha == 1:
        print("Sexta-feira ir jogar bola")
    case escolha if escolha == 2:
        print("Sábado ir ao cinema")
    case escolha if escolha ==3:
        print("Domingo ir ao zoológico")
    case _:
        print("Esolha invalida")
