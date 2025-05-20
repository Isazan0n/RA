num = int(input("Digite um número inteiro positivo: "))


if num < 2:
    print(f"{num} não é um número primo.")
else:
    for i in range(2, num):
        if num % i == 0:
            print(f"{num} não é um número primo.")
            break
    else:
        print(f"{num} é um número primo.")