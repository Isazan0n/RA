a = int(input("Digite o primeiro lado do triangulo: "))
b = int(input("Digite o segundo lado do triangulo: "))
c = int(input("Digite o terceiro lado do triangulo: "))

if a!=b==c or a==b!=c or a==c!=b:
    print("Triângulo isósceles")
elif a==b==c:
    print("Triângulo equilátero")
elif a!=b!=c:
    print("Triângulo escaleno")