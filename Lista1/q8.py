"""8. Leia a idade do usuário e classifique-o em:
 Criança – 0 a 12 anos
 Adolescente – 13 a 17 anos
 Adulto – acima de 18 anos (se o usuário
digitar um número negativo, mostrar a
mensagem que a idade é inválida)."""

idade = int(input("Digite sua idade: "))
if idade >= 18:
    print("Pela idade digitada de {} anos você já é adulto".format(idade))
elif idade <= 17 and idade >= 13:
    print("Pela idade digitada de {} anos você é adolescente".format(idade))
else:
    print("Pela idade digitada de {} anos você ainda é criança".format(idade))