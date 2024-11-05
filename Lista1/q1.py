""" 1. Ler uma temperatura em graus Celsius e apresentá-la convertida em graus Fahrenheit.
Usar a fórmula de conversão padrão F = (9 * C + 160) / 5, na qual F é a temperatura em Fahrenheit
e C é a temperatura em graus Celsius. """

C = float(input("Informe o valor em Celsius: "))
F = (9 * C + 160) / 5
print("A temperatura de {}ºC é igual a {}ºF".format(C, F))