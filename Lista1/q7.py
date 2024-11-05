"""7. Leia dois números inteiros e informe qual deles é o maior. Se os números forem iguais, mostrar esta informação na tela."""

numero1 = int(input("Digite o primeiro numero: "))
numero2 = int(input("Digite o segundo numero: "))
if numero1 == numero2:
    print("O primeiro número digitado: {} é igual ao segundo número digitado: {}".format(numero1, numero2))
elif numero1 > numero2:
    print("O primeiro número digitado: {} é maior que o segundo número digitado: {}".format(numero1, numero2))
else:
    print("O segundo número digitado: {} é maior que o primeiro número digitado: {}".format(numero2, numero1))