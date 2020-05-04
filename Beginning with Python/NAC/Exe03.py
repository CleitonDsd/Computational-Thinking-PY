
# MMC

numero1 = int(input("Digite um número: "))
numero2 = int(input("Digite outro número: "))
soma = 0
auxiliar = 0

if numero1 < 0 or numero2 < 0:
    print("Erro: digite um número positivo!")
else:

    if numero1 < numero2:
        auxiliar = numero1
        numero1 = numero2
        numero2 = auxiliar

    soma = numero1

    while soma % numero2 != 0:
        soma += numero1

print("MMMC (", numero1, ", ", numero2,"): ", soma)