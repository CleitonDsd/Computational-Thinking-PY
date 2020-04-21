binario = int(input("Informe o número binário: "))

potenciaDois = 1
acumulador = 0
while binario != 0:
    digito = binario % 10
    binario = binario // 10
    #print(digito * potenciaDois)
    acumulador += digito * potenciaDois
    potenciaDois *= 2

print(acumulador)