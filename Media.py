soma = 0
cont = 0

while True:
    num = int(input("Insira um numero (digite um numero negativo): "))

    if num < 0:
        break

    soma += num
    cont += 1

if cont > 0:
    media = soma / cont
    print("A media dos numeros informados é: ", media)
else:
    print("Nenhum numero foi fornecido.")