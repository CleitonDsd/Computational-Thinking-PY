import Exe01_funcoes as f

num = 2
contador = 0

while contador < 10:
    if f.ehPrimo(num) == True:
        print(num)
        contador = contador + 1

    num = num + 1




