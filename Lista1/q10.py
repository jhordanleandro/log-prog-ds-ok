"""10. Leia um número inteiro e apresentar as seguintes mensagens:
 “O valor está na faixa permitida”, caso o valor esteja entre 1 e 9
 “O valor está fora da faixa permitida”, caso o valor seja menor que 1 OU maior que 9."""

numero = int(input("Digite um número: "))
if numero >= 1 and numero <= 9:
    print("O valor {} está na faixa permitida!".format(numero))
else:
    print("O Valor {} está fora da faixa permitida!".format(numero))