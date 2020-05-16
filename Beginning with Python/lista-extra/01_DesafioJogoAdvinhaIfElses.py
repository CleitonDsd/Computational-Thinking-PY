# Faça um jogo de adivinhação. Você vai ter 3 chances
# para descobrir um número sorteado aleatoriamente entre 1 e 10,
# a cada tentativa o algoritmo informa se o número sorteado
# é maior ou menor do que o número escolhido.

import random

sorteado = random.randrange(1, 11)

chute = int(input("1.Chute um número: "))

#verifica se você acertou ou errou o  numero sorteado

if (chute == sorteado):
    print("Você acertou o número!!! \nNúmero: ", chute)

#Resultados > que N randomico
elif (chute > sorteado):
    print("O número chutado é MAIOR do que o sorteado")
    print("2. {Digite novamente} ")
    chute = int(input("Chute um número: "))

    if (chute == sorteado):
        print("Você acertou o número!!! \nNúmero: ", chute)
    elif(chute > sorteado):
        print("O número chutado é MAIOR do que o sorteado")
        print("3. {Digite novamente} ")
        chute = int(input("Chute um número: "))

        if (chute == sorteado):
            print("Você acertou o número!!! \nNúmero: ", chute)
        elif (chute > sorteado):
            print("O número chutado é MAIOR do que o sorteado")
            print("VOCÊ PERDEU! ")

#Resultados < que N randomico
elif (chute < sorteado):
    print("O número chutado é MENOR do que o sorteado")
    print("2. Digite novamente: ")
    chute = int(input("Chute um número: "))

    if (chute == sorteado):
        print("Você acertou o número!!! \nNúmero: ", chute)
    elif (chute < sorteado):
        print("O número chutado é MENOR do que o sorteado")
        print("3. {Digite novamente} ")
        chute = int(input("Chute um número: "))

        if (chute == sorteado):
            print("Você acertou o número!!! \nNúmero: ", chute)
        elif (chute < sorteado):
            print("O número chutado é MENOR do que o sorteado")
            print("VOCÊ PERDEU! ")

#Usando três variáveis, com operador booleano.
acertou = False
if chute > sorteado:
    print("Tente um número MENOR")
elif chute < sorteado:
    print("Tente um número MAIOR")
else:
    print("PARABÉNS! Você acertou!")
    acertou = True

if not acertou: #acertou == false
    chute = int(input("Chute um outro número: "))
    if chute > sorteado:
        print("Tente um número MENOR")
    elif chute < sorteado:
        print("Tente um número MAIOR")
    else:
        print("PARABÉNS! Você acertou!")
        acertou = True

if not acertou:
    chute = int(input("Chute um outro número: "))
    if chute == sorteado:
        print("PARABÉNS! Você acertou!")
    else:
        print("O número era ", sorteado)
        print("GAME OVER!")
