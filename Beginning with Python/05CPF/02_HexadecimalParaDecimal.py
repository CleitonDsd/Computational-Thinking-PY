#hexadecimal para decimal
soma = 0

numHexa = input("Digite hexa: ")

#funcao len retorna a qtd de caracteres da string
pos = len(numHexa) - 1
pot = 1
valor = 0

while pos >= 0:
    c = numHexa[pos]

    if c == "A":
        valor = 10
    elif c == "B":
        valor = 11
    elif c == "C":
        valor = 12
    elif c == "D":
        valor = 13
    elif c == "E":
        valor = 14
    elif c == "F":
        valor = 15
    else:
        valor = int(c)

    soma = soma + valor * pot
    pos = pos - 1
    pot = pot * 16

print("Resp", soma)

