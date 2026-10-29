pessoa = {
    "id": 1,
    "nome": "Renan",
    "email": "renan.a.peixinho@gmail.com"
}

print(f"ID: {pessoa["id"]}")
print(f"Nome: {pessoa["nome"]}")
print(f"E-mail:{pessoa["email"]}")

print(pessoa.keys())

print(pessoa.items())

print(pessoa.get("nom", "Nome não encontrado" ))

print(pessoa.items())
print(pessoa.pop("email", "E-mail não encontrado"))
print(pessoa.items())

print(pessoa.items())
print(pessoa.setdefault("idade", 16))
print(pessoa.items())


print(pessoa.items())
print(pessoa.popitem())
print(pessoa.items())




print(pessoa.items())
print(pessoa.update({"nome": "Carlos", "idade": 35}))
print(pessoa.items())

pessoa_clone = pessoa.copy()
print(pessoa_clone.items())


print(pessoa.items())
print(pessoa.clear())
print(pessoa.items())