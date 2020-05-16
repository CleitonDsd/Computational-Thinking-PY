# números primos

def ePrimo (num):

    if num == 1: #não é primo[
        return False

    else:
        div = 2
        while num % 2 != 0:
            div = div + 1

    