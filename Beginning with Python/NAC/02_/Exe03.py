# Ainda sobre datas, escreva uma função que recebe duas datas (cada uma delas sendo re-
# presentada por 3 números inteiros) e retorna a quantidade de dias existentes entre as duas
#
# datas. Por exemplo, você poderia informar a data de seu aniversário e a data de hoje, sua
# função retornará a quantidade de dias que você viveu.

#verifica se o ano é bissexto
def anoBissexto(ano):
    return ano % 4 == 0 and (ano % 100 != 0 or ano % 400 == 0)

#Retornar o dia do Ano decorrido
def diferencaEntreDatas (diaDataInicial, mesDataInicial, anoDataInicial, diaDataFinal, mesDataFinal, anoDataFinal):

    numeroDeDiasDataInicial = diaDataInicial
    numeroDeDiasDataFinal = diaDataFinal
    contadorMeses = 1

    anoDataFinal = anoDataFinal * 365.25
    anoDataInicial = anoDataInicial * 365.25

    quantidadeAnosBissextos = anoDataInicial + anoDataFinal / 4

    numeroDeDiasDataInicial += anoDataInicial
    numeroDeDiasDataFinal += anoDataFinal

    while contadorMeses < mesDataInicial:

        if contadorMeses in (1, 3, 5, 7, 8, 10, 12):
            numeroDeDiasDataInicial += 31
            numeroDeDiasDataFinal += 31

        elif contadorMeses in (4, 6, 9, 11):
            numeroDeDiasDataInicial += 30
            numeroDeDiasDataFinal += 30

        elif contadorMeses == 2:
            numeroDeDiasDataInicial += 28
            numeroDeDiasDataFinal += 28

        contadorMeses += 1

        diferenca = numeroDeDiasDataFinal - numeroDeDiasDataInicial
    return print("Dias de diferença: ", diferenca)

diferencaEntreDatas (1, 11, 2000, 3, 6, 2020)