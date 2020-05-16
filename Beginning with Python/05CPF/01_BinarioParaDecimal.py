#Converte um binario para decimal
binario = int(input("Informe o numero binario: "))

potDois = 1
acumulador = 0

while binario != 0:
    digito = binario % 10
    binario = binario // 10
    #print(digito * potDois)
    acumulador = acumulador + digito * potDois
    potDois = 2 * potDois   

print(acumulador)
