

valor = float(input("Digite um valor: "))
desconto = float(input("Valor do desconto: "))

acrescimo = desconto

calcularDesconto = (valor * desconto ) / 100
calcularAcrescimo = valor  + (valor * acrescimo/100)
print("Valor total ", calcularDesconto, "| desconto de ", desconto, "%")
print("Valor total", calcularAcrescimo, "| acréscimo de ", acrescimo, "%")