
i = 0
soma = 0
while (i < 5):
      numero = int(input("Digite um número: "))
      if (numero % 2 == 0):
          soma = numero + numero
      i += 1
      print("== Numeros Pares ==")
      while(numero % 2 == 0) and (i < 5):
          print(numero)
          i += 1
print("Soma dos números pares: ", soma)



mediaAnoAnterior = float(input("Média do ano passado: "))
consumoVigente = float(input("Consumo Vigente: "))

valorUnitario = 0

if (consumoVigente < 20):
    valorUnitario = 2.0

elif(consumoVigente < 35):
    valorUnitario = 3.5

elif(consumoVigente < 50):
    valorUnitario = 5.5
else:
    valorUnitario = 7.0

valorConta = consumoVigente * valorUnitario

if consumoVigente < mediaAnoAnterior:
    print("Valor: " + valorConta)
    desconto = valorConta * 0.2
    print("Desconto: ", desconto)
    print("Valor final: ", valorConta - desconto)

elif (consumoVigente > mediaAnoAnterior * 1.1):
    print("Valor: ", valorConta)
    multa = valorConta * 0.3
    print("Multa: ", multa)
    print("Valor Final: ", valorConta + multa)

else:
    print("Valor: ", valorConta)
