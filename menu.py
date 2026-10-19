
        
def menu():
        print("=== Menu ===")
        print("1 - Ver mensagem")
        print("2 - Sair")

def escolheu(escolha):
    match escolha:
        case "1":
            print("Bem-Vindo")
        case "2":
            print("Saindo...")
        case _:
            print("Opção inválida. Tente novamente.")

while True:
    menu()
    escolha = input("Escolha uma opção: ")
    escolheu(escolha)
    if escolha == "2":
        break




