salario = float(input("Digite seu salario: "))
imposto1 = salario * 0.15
imposto2 = salario * 0.25

if 20.000 < salario > 50.000:
    salario = salario - imposto1
    print(f"{salario:.2f}")
elif 50.001 > salario:
    salario = salario - imposto2
    print(f"{salario:.2f}")
else:
    print(salario)