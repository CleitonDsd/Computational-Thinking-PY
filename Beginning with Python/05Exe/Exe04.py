def contadigito (n, d):

    contador = 0

    while n != 0:
        dig = n % 0
        if dig == d:
           contador += 1

        n = n / 10


num = 1259035
d = 5
qtd = contadigito(num, d)
print(qtd)