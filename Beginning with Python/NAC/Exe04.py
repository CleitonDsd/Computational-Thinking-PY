# MDC

numero1 = int(input("Digite um número: "))
numero2 = int(input("Digite outro número: "))

if numero1 < 0 or numero2 < 0:
    print("Erro: digite um número positivo!")
else:


    contador = 2
    auxiliar = 0
    mmc = 0
    while numero2 != 0:
        resto = numero1 % numero2
        numero1 = numero2
        numero2 = resto
        print("")
        print("MDC: ", numero1)