#Retornar a quantidade de vogais


def quantidadeVogais(frase):
    totalVogais = 0
    for palavra in frase:
        for letra in palavra:
            if letra in 'AEIOU' or letra in 'aeiou':
                totalVogais += 1

    print('Total de vogais: ', totalVogais)

quantidadeVogais('cleiton')