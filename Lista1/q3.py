"""3. Leia a base e altura de um triângulo, calcule e apresente o valor da área. Utilize
a fórmula: area = (base * altura) / 2."""

base = int(input("Informe o base: "))
altura = int(input("Informe o altura: "))
area = (base * altura) / 2
print("O triângulo de base {} unidades e altura {} unidades tem uma área total de {} unidades".format(base, altura, area))