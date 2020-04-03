
dia = int(input("Dia: "))
mes = int(input("Mês: "))
ano = int(input("Ano: "))

dataValida = True

if (dia < 1) or (dia > 31) or (mes < 1) or (mes > 12):
    dataValida = False
elif(dia == 31) and (mes == 4 or mes == 6 or mes == 9 or mes == 11):
    dataValida = False
elif(mes == 2 and dia >= 29):
    #teste do ano bissexto
    if dia > 29:
        dataValida = False
    else:
        if (ano % 4 != 0):
            dataValida = False
        elif (ano % 100 == 0) and (ano % 400 != 0):
            dataValida = False

if dataValida:
    print("Data Válida")
else:
    print("Data Inválida")
