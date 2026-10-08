senha = "cabecao"

while True:
    senhaCorreta = input("Digite a senha: \n")
    if senhaCorreta == senha:
        print("Acesso liberado\n ")
        break
    else:
        print("Senha incorreta tente novamente!\n ")
    
    