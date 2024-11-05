"""6. Leia um número inteiro e informe se ele é positivo ou negativo (considere zero como positivo)."""

numero = int(input("Digite um número inteiro: "))
if numero % 2 == 0:
    print("O número {} é positivo!".format(numero))
elif numero == 0:
    print("O número {} é positivo!".format(numero))
else:
    print("O número {} é negativo!".format(numero))