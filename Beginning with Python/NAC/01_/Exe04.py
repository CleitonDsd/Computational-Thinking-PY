# MDC

numero1 = int(input("Digite um número: "))
numero2 = int(input("Digite outro número: "))
resto = 0
auxiliar = 0

if numero1 < 0 or numero2 < 0:
    print("Erro: digite um número positivo!")
else:


    resto = numero1 % numero2

    while resto != 0:
        numero1 = numero2
        numero2 = resto
        resto = numero1 % numero2

print("MDC (", numero1, ", ", numero2,"): ", numero2)