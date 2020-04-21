# Um número inteiro positivo n é denominado primo se existirem apenas dois divisores inteiros
# positivos dele: o 1 e o próprio n. Escreva um algoritmo que recebe um inteiro n e verica
# se n é primo ou não.

numero = int(input("Digite um número: "))

contador = 0
numeroDivisores = 0
while contador <= numero:
    contador+= 1
    if (numero % contador == 0):
        numeroDivisores +=1


if(numeroDivisores == 2):
    print("Número Primo")
else:
    print("Número não é Primo")
