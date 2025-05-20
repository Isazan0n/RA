acomulador = 0
contador = 0

while True:
    n = float(input("Digite um numero (se ele for negativo, o programa irá parar): "))

    if n < 0:
        break
    if n % 2 == 0:
        acomulador += n
        contador += 1

if contador > 0:
    media = acomulador / contador
    print("A soma dos números pares é: ", acomulador)
    print("A media dos numeros pares é: ", media)
else:
    print("Nenhum numero par foi digitado.")