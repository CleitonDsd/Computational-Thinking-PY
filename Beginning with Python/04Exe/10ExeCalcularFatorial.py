

numero = int(input("Digite um número: "))

contador = 1
fatorial = 1
while contador <= numero:
    fatorial *= contador
    contador += 1

print("Fatorial de ", numero,"! é: ",fatorial)