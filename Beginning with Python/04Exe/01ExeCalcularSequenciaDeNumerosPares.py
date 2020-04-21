# Dada uma sequência de números inteiros onde o último elemento é o 0, escreva um algoritmo
# que calcula a soma dos números pares da sequência.


numero = int(input("Digite um número: "))

while numero % 2 != 0:
    numero = int(input("Digite um número: "))
    if numero % 2 == 0:
        soma = soma + numero

print("Soma dos Numeros Pares: ", soma)