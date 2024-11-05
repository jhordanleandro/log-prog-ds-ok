"""2. Ler os valores de comprimento, largura e altura e apresentar o valor do volume de uma caixa
retangular. Utilize a fórmula: volume = comprimento * largura * altura."""

comprimento = float(input("Informe o comprimento: "))
largura = float(input("Informe o largura: "))
altura = float(input("Informe o altura: "))
volume = comprimento * largura * altura
print("O valor do volume é de {} unidades".format(volume))