# Escrever um algoritmo que leia dois valores inteiro distintos e informe qual é o maior ou se
# houve um empate.


valorA = float(input("Digite o valor A: "))
valorB = float(input("Digite o valor B: "))

if (valorA > valorB):
    print("Valor A é maior que o Valor B")
elif(valorB > valorA):
    print("Valor B é maior que o Valor A")
elif(valorB == valorA):
    print("Valor A é igual ao Valor B")