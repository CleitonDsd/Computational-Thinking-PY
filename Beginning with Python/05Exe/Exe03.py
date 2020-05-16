import Exe01_funcoes as funcoes

num = 1
while num <= 50_000:
    if funcoes.ehPerfeito(num):
        print(num)

    num = num + 1