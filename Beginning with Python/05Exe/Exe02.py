import Exe01_funcoes as f
num = 2

contador = 0
while contador < 100:

    if  f.ePrimo(num) == True:
        print(num)
        contador += 1

    num += 1
