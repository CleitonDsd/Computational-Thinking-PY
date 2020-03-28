# A raiz quadrada é uma operação que apenas aceita números positivos. Escreva um algoritmo
# que lê um número qualquer e retorna a raiz quadrada desse número se possível. Use a função
# math.sqrt(<numero>) para calcular a raiz quadrada em Python. Note que, para usar essa função,
# você terá que importar o módulo math antes.

import math

valor = int(input("Digite um valor: "))

if (valor > 0):
    raizQuadrada = math.sqrt(valor)
    print("Raiz quadrada de ", valor, " é V", raizQuadrada)
else:
    print("Não é posível calcular raiz quadrada onde N <= 0")