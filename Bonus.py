salario = float(input("Digite seu salário: "))
tempo = int(input("Digite o seu tempo de serviço em anos: "))

if tempo >= 5:
    salario = salario + (salario * 0.05)
    print("Novo salário: ", salario)
else:
    print("Salário: ", salario)