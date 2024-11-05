"""4. Leia as informações de um consórcio, tal como o número total de prestações, a quantidade total
de prestações pagas e o valor de cada prestação. Calcule e mostre na tela o total pago pelo
consorciado e o saldo devedor."""

numeroTotalPrestacao = int(input("Digite o número de prestações: "))
quantidadePrestacaoPaga = int(input("Digite o número de prestações pagas: "))
valorCadaPrestacao = float(input("Digite o valor de cada prestação: "))
valorTotalConsorcio = numeroTotalPrestacao * valorCadaPrestacao
valorTotalPago = quantidadePrestacaoPaga * valorCadaPrestacao
saldoDevedor = valorTotalConsorcio - valorTotalPago
print("O consorciado adquiriu um consorcio com {} prestações tendo pago um valor total de R${} e ficando com um saldo devedor de R${}".format(numeroTotalPrestacao, valorTotalPago, saldoDevedor))

