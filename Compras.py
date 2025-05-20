total = float(input("Digite o valor total gasto em compras: "))
desconto = total * 0.10

if total >= 100.00:
    total = total - desconto
    print("Valor a ser pago: ", total)
else:
    print("Valor a ser pago: ", total)