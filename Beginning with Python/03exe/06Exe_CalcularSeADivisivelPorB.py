# Faça um programa para ler dois números inteiros A e B e informar se A é divisível por B.

valorA = int(input("Valor A: "))
valorB = int(input("Valor B: "))


if (valorA % valorB == 0):
    print(valorA, " É DIVISIVEL por", valorB)
else:
    print(valorA, " não é divisivel por", valorB)