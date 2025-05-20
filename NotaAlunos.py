media = []
abaixoMedia = []

num = 0
num2 = 0

quant = int(input("Digite a quanidade de alunos: "))

for i in range(quant):
    nota = int(input("Digite a nota da primeira prova: "))
    nota2 = int(input("Digite a nota da segunda prova: "))
    notaFinal = (nota + nota2) / 2

    if notaFinal >= 60:
        num = num + 1
        media.append(num)
    else:
        num2 = num2 + 1
        abaixoMedia.append(num2)

tamanho2 = len(abaixoMedia)
tamanho = len(media)
print(f"Alunos que estão na media: {tamanho}")
print(f"Alunos que estao abaixo da media: {tamanho2}")