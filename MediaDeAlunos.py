cont = 0
soma_medias = 0

while cont < 50:
    nome = str(input("Digite seu nome do aluno: "))
    n1 = float(input(f"{nome}, digite sua nota: "))
    n2 = float(input(f"{nome}, digite sua nota: "))
    n3 = float(input(f"{nome}, digite sua nota: "))
    n4 = float(input(f"{nome}, digite sua nota: "))

    media = (n1 + n2 + n3 + n4) / 4
    soma_medias += media
    print("A media das notas de", nome," é ", media)

    if media >= 7:
        print(f"{nome} foi aprovado(a)!")
    else:
        print(f"{nome} foi reprovado(a)!")

    cont += 1

total_medias = soma_medias/ cont
print("A media total é: {total_medias:.2f}")