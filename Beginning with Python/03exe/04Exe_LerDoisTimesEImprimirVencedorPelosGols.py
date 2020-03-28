# Escreva um algoritmo para ler o nome de 2 times e o número de gols marcados em uma
# partida. Escrever o nome do vencedor. Caso não haja vencedor deverá ser impresso a
# palavra EMPATE.

timeA = input("Time A: ")
golsMarcadosA = int(input(timeA + "Gols marcados (N): "))
timeB = input("Time B: ")
golsMarcadosB = int(input(timeB + "Gols marcados (N): "))

if (golsMarcadosA > golsMarcadosB):
    print(timeA, " ", golsMarcadosA, " X ", golsMarcadosB, " ", timeB , " | ", timeA, " GANHOU!")

elif (golsMarcadosB > golsMarcadosA):
    print(timeA, " ", golsMarcadosA, " X ", golsMarcadosB, " ", timeB, " | ", timeB, " GANHOU!")

elif (golsMarcadosA == golsMarcadosB):
    print(timeA, " ", golsMarcadosA, " X ", golsMarcadosB, " ", timeB, " | ", " EMPATE!")