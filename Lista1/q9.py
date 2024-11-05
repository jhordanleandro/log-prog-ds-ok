"""9. Leia dois números reais e uma operação, e com isso imprima o resultado de acordo com a
operação escolhida pelo usuário: adição,subtração, multiplicação e divisão. Caso seja
informada operação inválida, mostrar uma mensagem na tela informando."""

numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))
operacao = str(input("Escolha o número da operação que deseja efetuar: 1 (adição), 2 (subtração), 3 (multiplicação) ou 4 (divisão): "))

def testeOperacao(operacao):
    match operacao:
        case '1':
            return numero1 + numero2
        case '2':
            return numero1 - numero2
        case '3':
            return numero1 * numero2
        case '4':
            return numero1 / numero2
        case '5':
            return "Operação Invalída!"

print(testeOperacao(operacao))
