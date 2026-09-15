
def calculadora(num1, num2, operador):
    if operador == "+":
        return num1 + num2
    elif operador == "-":
        return num1 - num2
    elif operador == "*":
        return num1 * num2
    elif operador == "/":
        if num2 == 0:
            print("Erro não pode ser dividido por 0!")
        return num1 / num2
    
numero1 = 10
numero2 = 20
operador = "*"
print(f"{numero1} + {numero2} = {calculadora(numero1, numero2, operador)}")