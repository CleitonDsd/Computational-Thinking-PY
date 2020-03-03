# Uma pessoa tem em seu guarda roupas x camisas, y calças e z pares de sapato.
# Escreva um algoritmo que calcula de quantas maneiras diferentes ele pode se vestir.
# Seu algoritmo deverá ler o número de camisas, o número de calças e o número de sapatos.


numeroCamisas = int(input("Quantidade de camisas: "))
numeroCalcas = int(input("Quantidade de calças: "))
numeroSapatos = int(input("Quantidade de sapatos: "))

quantidadeDiferentes = numeroCamisas * numeroCalcas * numeroSapatos

print("Quantidade diferentes de combinações: ", quantidadeDiferentes)

# x -> y -> z
# y -> z -> x
# z -> x -> y
