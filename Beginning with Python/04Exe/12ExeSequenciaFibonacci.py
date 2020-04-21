

anterior = 0
atual = 0

proximo = atual + anterior

while (atual < 50):
    print(anterior)
    atual += anterior
    anterior = atual - anterior

    if(atual == 0):
        atual += 1