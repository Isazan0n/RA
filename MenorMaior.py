a = []

for i in range(10):
    num = int(input("Digite um numero inteiro: "))
    a.append(num)

maiorValor = max(a)
menorValor = min(a)

print(f"Maior numero digitado: {maiorValor}")
print(f"Menor numero digitado: {menorValor}")