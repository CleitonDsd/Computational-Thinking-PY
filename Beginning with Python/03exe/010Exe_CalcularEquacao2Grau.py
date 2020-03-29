# 10. Uma equação de 2o grau é da forma: ax2 + bx + c = 0, onde a 6= 0. Escreva um algoritmo
# que recebe os três coecientes da equação, calcula e imprime as raízes reais se for possível.
import math
print("== COEFICIENTES ==")
valorA = float(input("A: "))
valorB = float(input("B: "))
valorC = float(input("C: "))

delta = valorB**2 - 4 * valorA * valorC

x1 = (-valorB) + (math.sqrt(delta) / (2 * valorA))
x2 = (-valorB) - (math.sqrt(delta) / (2 * valorA))

print("Delta: ", delta)
print("X1: ", x1)
print("X2", x2)

# //incompleto