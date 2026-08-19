'''for posicao in range(1,6):
    print(posicao)'''
'''for i in range(6):
    print(i)'''
'''for i in range(0,11,2):
    print(i)'''

numero = int(input("coloque o numero"))
for i in range(2, numero):
    if numero % i ==0:
        print(f"{numero}O não é primo (divisivel por {i}.)")
        break
    else:
        print(f"{numero} é um nùmero primo")