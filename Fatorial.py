num = int(input("Digite um numero positivo e inteiro: "))
fat = 1

for i in range (num , -1, -1):
    fat = fat * i

print(fat)