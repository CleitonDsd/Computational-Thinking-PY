# Em uma prova de concurso com 70 questões haviam 20 pessoas concorrendo. Sabendo que
# cada questão vale 1 ponto, escreva um algoritmo que lê a pontuação da prova obtida de cada
# um dos candidatos e calcula:

# a) a maior e a menor nota
# b) o percentual de candidatos que acertaram até 20 questões, o percentual que acertaram
# de 21 a 50 e o percentual que acertou acima de 50 questões


#nota do 1° candidato
nota = int(input("Digite a Nota: "))
maior = nota
menor = nota

somaAte20Questoes = 2
somaAte50Questoes = 2

#notas dos demais candidatos
contador = 2
while contador <= 4:
    nota = int(input("Digite a Nota: "))
    if (nota < menor):
       menor = nota
    if (nota> maior):
       maior = nota

       contador = contador + 1

    if(nota <= 20):
        somaAte20Questoes += 1
    elif(nota >= 21 or nota <= 50):
        somaAte50Questoes += 1

print("Maior Nota: ", maior)
print("Menor Nota: ", menor)
percentual = (somaAte20Questoes / 70) * 100
print("Percentual dos que acertaram até 20 questões: ", percentual)
percentual = (somaAte50Questoes / 70) * 100
print("Percentual dos que acertaram até 50 questões: ", percentual)




