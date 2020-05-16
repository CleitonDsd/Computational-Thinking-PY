

def contadigito(n, d):
    contador = 0
    while n != 0:
        dig = n % 10
        if dig == d:
            contador = contador + 1
        n = n // 10

    return contador


#Resolução do item b
a = int(input("Informe a: "))
b = int(input("Informe b: "))
digi = 1
qtd_a = 0
qtd_b = 0

while qtd_a == qtd_b and digi <= 9:
    qtd_a = contadigito(a, digi)
    qtd_b = contadigito(b, digi)
    digi = digi + 1

if qtd_a != qtd_b:
    print("Não formam uma permutação!")
else:
    print("Eles formam uma permutação")






