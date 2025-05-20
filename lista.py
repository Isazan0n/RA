# Lista para armazenar os nomes dos alunos
nomes_alunos = []
num = 0
quant= int(input("Digite a quantidade de alunos:"))

#Loop para ler a quantidade de alunos
for i in range(quant):
    nome = input(f"Digite o nome do aluno {i + 1} ")
    nomes_alunos.append(nome)

#Exibindo os nomes registrados
print("\nNomes dos alunos registrados:")
for nome in nomes_alunos:
    num = num + 1
    print(f"{num}: {nome}")

