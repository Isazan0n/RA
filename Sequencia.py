n = int(input("Digite o número que deseja imprimir: "))

a, b = 0, 1
count = 0

while count < n:
    print(a, end=' ')
    a, b = b, a + b
    count += 1
    