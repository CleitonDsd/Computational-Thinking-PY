# No problema de vericar se um número é primo ou não resolvemos contando o número
# de divisores. Também podemos pensar em resolver este problema encontrando um divisor
# diferente de 1. Se tal divisor for o próprio n, signica que n é primo, caso contrário, dizemos
# que ele não é primo. Pensando nessa ideia, escreva um algoritmo que verica se n é primo
# ou não. Ao invés do comando for use o comando while

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
