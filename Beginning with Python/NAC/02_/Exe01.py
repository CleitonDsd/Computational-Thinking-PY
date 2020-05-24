# Uma data pode ser representada, de maneira bem simples, utilizando três números inteiros:
# dia, mes e ano. Sua tarefa neste exercício, é criar uma função que recebe como parâmetros
# três numeros inteiros representando uma data e um outro número inteiro representando uma
# quantidade de dias. Essa quantidade de dias, deverá ser somada a essa data retornando uma
# data futura.

# Por exemplo, suponha o dia 13/05/2020 e 25 dias que serão somados, sua
# função deverá retornar 08/06/2020. Retorne o resultado da função como uma tupla.



# final dos meses
ultimaDiaMês = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
def verificarAnoBissexto(ano):
    if ano % 400 == 0:
        ultimaDiaMês[1] = 29
    elif ano % 100 != 0 and ano % 4 == 0:
        ultimaDiaMês[1] = 29


# retornar o dia de amanhã
def retornarDiaAmanha(dia, mes, ano):

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






















































#
# #função para somar dias a uma data e retornar a data somando os dias acrescentados
# def calcularDiasNaData(dia, mes, ano, diasAcrescentados):
#
#     contador = 1
#     while contador <= diasAcrescentados:
#         # acrescentando, dia, mês e ano
#         if (dia == 30 or dia == 31) and mes == 12:
#             dia = 1
#             mes = 1
#             ano += 1
#
#         # dia acrescentando mês
#         elif (dia == 30 or dia == 31) and mes <= 11:
#             dia = 1
#             mes += 1
#
#         # dia, acrescentando dia
#         elif (dia >= 1 or dia <= 29) and (mes >= 1 or mes <= 12):
#             dia += 1
#
#         print(contador)
#         contador += 1
#
#     print("Data de amanhã: ", dia, "/", mes, "/", ano)
#
# calcularDiasNaData(27, 4, 2020, 34)

