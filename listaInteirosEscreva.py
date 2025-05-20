a = []

num1 = 0

for i in range(10):
    num = int(input("Digite um numero inteiro: "))
    a.append(num)

print("\nLista a:")
for num in a:
    num1 = num1 + 1
    print(f"{num1}° numero inteiro: {num}")