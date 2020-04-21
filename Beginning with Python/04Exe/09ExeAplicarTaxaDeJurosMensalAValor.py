# Dados um montante em dinheiro inicial d, uma taxa de juros mensal j e um período de
# tempo em meses t, escreva um algoritmo que calcula o valor nal em dinheiro se d car
# aplicado a taxa de juros j durante t meses.


montanteInicial = float(input("Digite o Montante Inicial (R$): "))
jurosMensal = float(input("Digite a taxa de Juros Mensais: "))
meses = int(input("Digite a quantidade de Meses: "))

print("Juros Mensais(%): ", jurosMensal, "%")
jurosMensal /= 100

jurosTotal = montanteInicial * jurosMensal * 6
jurosTotal /= meses

print("Juros Total(R$): ",jurosTotal)

valorTotal = jurosTotal + montanteInicial
print("Valor Total(R$): ", valorTotal, " aplicado em ", meses, " meses ")

