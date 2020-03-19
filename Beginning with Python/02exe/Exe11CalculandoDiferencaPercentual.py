# Neste mês, João recebeu um aumento no salário, porém ele não sabe calcular o percentual
# de aumento. Você deverá escrever um algoritmo que recebe 2 números reais representando
# os salários antes e depois do aumento e deverá calcular e exibir o percentual de aumento que
# João obteve.

salarioAntesAumento = float(input("Digite o salário antes do aumento(R$): "))
salarioDepoisAumento = float(input("Digite o salário depois do aumento(R$): "))

calcularPorcentagem = (salarioDepoisAumento - salarioAntesAumento) / salarioAntesAumento
calcularPorcentagem = calcularPorcentagem * 100

print ("Salário antigo(R$): ", salarioAntesAumento, "\nSalário atual (R$): ", salarioDepoisAumento, "\nAumento Percentual: ", calcularPorcentagem, "%")