

#Retornar o dia do Ano decorrido
def diaDoAno (dia, mes, ano, diasAcrescentados):

    numeroDeDias = dia
    contadorMeses = 1

    while contadorMeses < mes:

        if contadorMeses in (1, 3, 5, 7, 8, 10, 12):
            numeroDeDias += 31

        elif contadorMeses in (4, 6, 9, 11):
            numeroDeDias += 30

        elif contadorMeses == 2:
            numeroDeDias += 28

        contadorMeses += 1

        totalDeDiasComAcrescimo = numeroDeDias + diasAcrescentados

    return print(totalDeDiasComAcrescimo)

#verifica se o ano é bissexto
def anoBissexto(ano):
    return ano % 4 == 0 and (ano % 100 != 0 or ano % 400 == 0)


def validarData (dia, mes, ano):

    #verifica se os meses abaixo tem dia equivalente a 31
    if mes in (4, 6, 9, 11) and dia == 31:
        return False
    # verifica se Fevereiro é >= 30, se sim, falso.
    if mes == 2 and dia >= 30:
        return False
    #caso fevereiro tenha 29 dias e o ano não é bissexto, falso
    if mes == 2 and dia == 29 and not anoBissexto(ano):
        return False
    return True



# retornar o dia de amanhã
def retornarDiaAmanha(dia, mes, ano):
    anoBissexto(ano)
    validarData(dia, mes, ano)
    diaDoAno(dia, mes, ano)

    contador = 1
    while contador < diaDoAno():
        # acrescentando, dia, mês e ano
        if (dia == 30 or dia == 31) and mes == 12:
            dia = 1
            mes = 1
            ano += 1
            print("Data de amanhã: ", dia, "/", mes, "/", ano)

        # dia acrescentando mês
        elif (dia == 30 or dia == 31) and mes <= 11:
            dia = 1
            mes += 1
            print("Data de amanhã: ", dia, "/", mes, "/", ano)

        # dia, acrescentando dia
        elif (dia >= 1 or dia <= 29) and (mes >= 1 or mes <= 12):
            dia += 1
            print("Data de amanhã: ", dia, "/", mes, "/", ano)



diaDoAno(1, 11, 2020, 10)