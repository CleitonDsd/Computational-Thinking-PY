# Dizemos que um número natural n é palíndromo se o 1o algarismo de n é igual ao seu último
# algarismo, o 2o algarismo de n é igual ao penúltimo algarismo, e assim sucessivamente.
# Exemplos: 567765 e 32423 são palíndromos. 567675 não é palíndromo.


num = int(input("Digite um num: "))
ac = 0

while (num != 0):
    a = num % 10
    num = num // 10
    ac = ac * 10 + a

if num == ac:
    print("É palíndrome")

else:
    print("Não é palíndrome")