# Uma pessoa tem em seu guarda roupa x camisas, y calças e z pares de sapato. Escreva
# um algoritmo que calcula de quantas maneiras diferentes ele pode se vestir. Seu algoritmo
# deverá ler o número de camisas, o número de calças e o número de pares de sapato.

camisa = int(input("Digite a quantidade de camisa(s): "))
calca = int(input("Digite a quantidade de calça(s): "))
sapato = int(input("Digite a quantidade de sapato(s): "))

maneirasDiferentes = camisa * calca * sapato

print("Essa pessoa poderá se vestir de :", maneirasDiferentes, " maneiras diferentes")
