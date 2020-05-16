
def ehPrimo(num):
    if num == 1: #não é primo
        return False
    else:
        div = 2
        while num % div != 0:
            div = div + 1

        if num == div:
            return True
        else:
            return False


def ehPerfeito(num):
    soma = 0
    div = 1
    while num > div:
        if num % div == 0:
            soma = soma + div
        div = div + 1
    if soma == num:
        return True
    else:
        return False    