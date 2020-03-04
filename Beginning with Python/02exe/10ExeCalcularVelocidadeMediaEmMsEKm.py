# Escreva um algoritmo que calcula a velocidade média
# em M/S e em KM/H de um corredor, seu algortimo recebe
# como dados de entrada a distância em metros e o tempo
# sem segundos.


distanciaMetros = (float(input("Digite a distância percorrida em Metros: ")))

tempoSegundos = (int(input("Digite o tempo em Segundos: ")))

tempoHoras = tempoSegundos * 60

velocidadeMediaMS = distanciaMetros/tempoSegundos
print("A velocidade média durante ", distanciaMetros, "M é de ", velocidadeMediaMS, " M/S")

print("")

velocidadeMediaKM = velocidadeMediaMS * 3.6
print("A velocidade média durante ", distanciaMetros, "M é de ", velocidadeMediaMS, " KM/H")

