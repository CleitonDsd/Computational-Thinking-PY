
# MMC
numero1 = int(input("Digite um número: "))
numero2 = int(input("Digite outro número: "))

if numero1 < 0 or numero2 < 0:
    print("Erro: digite um número positivo!")
else:

    # fatoração simultânea
    contador = 2
    auxiliar = 0
    mmc = 0
    while contador <= numero2:

        auxiliar = numero1 * contador
        if (auxiliar % numero1 == 0):
            mmc = auxiliar
            contador = numero2 + 1

        contador+= 1
        print("")
        print("MMC: ", mmc)