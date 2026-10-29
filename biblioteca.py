livros = []
def mostrar_menu():
    print(f"\n1 - Cadastrar livro")
    print("2 - Consultar livro por ID")
    print("3 - Mostrar todos os livos")

    print("4 - Sair do Programa")

def  cadastrar_livro():
    id = int(input("\n Digite o ID do livro: "))
    nome = input("\nDigite o nome do livro: ")
    autor = input("\n Digite o nome do(a) autor(a): ")
    editora = input("\n Digite o nome da editora: ")
    livro = {
        "id": id,
        "nome": nome,
        "autor": autor,
        "editora": editora
    }
    livros.append(livro)

def busca_id(id):
    for livro in livros:
        if livro["id"] == id:
            print("\n livro encontrado")
            print(f"ID: {livro["id"]}")
            print(f"Nome: {livro["nome"]}")
            print(f"Autor: {livro["autor"]}")
            print(f"Editora: {livro["editora"]}")
        else:
            print("\nlivro não encontrado")

def mostrar_livros():
    for livro in livros:
        print(f"ID: {livro["id"]}")
        print(f"Nome: {livro["nome"]}")
        print(f"Autor: {livro["autor"]}")
        print(f"Editora: {livro["editora"]}\n")

def menu_escolha(escolha):
    match escolha:
        case "1":
            cadastrar_livro()
        case "2":
            id_livro =int(input("Digite o ID" ))
            busca_id(id_livro)
        case "3":
            mostrar_livros()

while True:
    mostrar_menu()
    escolha =input("\nDIgite a escolha ou [4] para sair: ")
    menu_escolha(escolha)
    if escolha.lower() == "4":
        break