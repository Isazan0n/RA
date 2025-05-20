num = int(input("Digite um numero: "))
maior = 0

for i in range(0,5):
    if num > maior:
        maior = num
        num = int(input("Digite outro numero: "))

print("Maior numeo digitado: ", maior)