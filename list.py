l = []
par = []
impar = []

soma = 0

for i in range (5):
    num = int(input("Digite um numero inteiro: "))
    l.append(num)
    soma = soma + num

    if num % 2 == 0:
        par.append(num)
    else:
        impar.append(num)

menorPar = min(par)
menorImpar = min(impar)

print(f"Menor par = {menorPar}")
print(f"Menor impar = {menorImpar}")

print(f"Somatorio dos numeros = {soma}")

media = soma / 5
print(f"Media = {media}")