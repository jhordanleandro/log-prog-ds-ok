"""5. Efetuar o cálculo da quantidade de litros de combustível gasto em uma viagem, utilizando um
automóvel que faz 12 Km por litro. Para obter o cálculo, o usuário deve fornecer o tempo gasto na
viagem e a velocidade média durante ela. Desta forma, será possível obter a distância percorrida
com a fórmula: distancia = tempo * velocidade. Tendo o valor da distância, basta calcular a
quantidade de litros de combustível utilizada na viagem, com a fórmula: litros_usados =
distancia / 12. O programa deve apresentar os valores da velocidade média, tempo gasto na
viagem, a distância percorrida e a quantidade de litros utilizada na viagem."""

tempoGastoViagem = int(input("Digite o tempo, em horas, gasto na viagem: "))
velocidadeMedia = float(input("Digite a velocidade média, em Kmh, da viagem: "))
distancia = tempoGastoViagem * velocidadeMedia
litrosUsados = distancia / 12
print("A velocidade média foi de {} Kmh onde o tempo gasto foi de {} horas onde foi percorrido uma distancia de {} Km e o consumo foi de {} litros de combustível".format(velocidadeMedia, tempoGastoViagem, distancia, litrosUsados))
