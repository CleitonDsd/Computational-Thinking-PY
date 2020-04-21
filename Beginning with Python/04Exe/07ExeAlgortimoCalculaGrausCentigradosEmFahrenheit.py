# conversão de graus Fahrenheit para centígrados é obtida pela fórmula C =
# 5
# 9
# (F − 32).
# Escreva um algoritmo que calcule e escreva uma tabela de graus centígrados em função de
# graus Fahrenheit que variem de 50 a 150 Fahrenheit de 1 em 1.

grausC = float(input("Digite a temperatura em C°: "))

grausF = (grausC  * 9/5) + 32

print(grausC,"° em Fahrenheit ", grausF,"f")