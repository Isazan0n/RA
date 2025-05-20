n = int(input("Digite um numero positivo: "))
soma: int

primeiroNumero = 1
soma = 0

while primeiroNumero <= n:
    soma += primeiroNumero
    primeiroNumero += 2

print(f"A soma dos impares é {soma}")

