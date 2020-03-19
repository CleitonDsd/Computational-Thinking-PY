# Dados o preço de um produto e um percentual de desconto, escreva um algoritmo que calcula
# e mostra o valor do desconto e o novo preço do produto dado o percentual. E se, ao invés
# de um desconto, fosse um aumento. O que muda no seu algoritmo?


valor = float(input("Digite um valor: "))
desconto = float(input("Valor do desconto: "))

acrescimo = desconto

calcularDesconto = (valor * desconto ) / 100
calcularAcrescimo = valor  + (valor * acrescimo/100)
print("Valor total ", calcularDesconto, "| desconto de ", desconto, "%")
print("Valor total", calcularAcrescimo, "| acréscimo de ", acrescimo, "%")