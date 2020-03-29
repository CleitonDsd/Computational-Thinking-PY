# Escreva um algoritmo que calcule o que deve ser pago por um produto, considerando o preço
# normal de etiqueta e a escolha da condição de pagamento. Utilize os códigos da tabela a
# seguir para ler qual a condição de pagamento escolhida e efetuar o cálculo adequado.
# código condição de pagamento
# 1 A vista em dinheiro ou cheque, recebe 10% de desconto
# 2 A vista no cartão de crédito, recebe 5% de desconto
# 3 Em duas vezes, preço normal de etiqueta sem juros
# 4 Em quatro vezes, preço normal de etiqueta mais juros de 7%

valorProduto = float(input("Digite o valor do produto (R$): "))

print("== Forma de Pagamento ==")
print("1 - À vista (dinheiro ou cheque) 10% de desconto")
print("2 - À vista (cartão de crédito) 5% de desconto")
print("3 - Parcelado 2x (sem juros)")
print("4 - Parcelado 4x (mais 7% de juros)")
print("==========================")

formaPagamento = input("Digite a forma de pagamento(N): ")

if (formaPagamento == "1"):
    precoDesconto = valorProduto * 0.10
    precoTotal = valorProduto - precoDesconto
    print("Valor do Produto (R$): ", valorProduto)
    print("Valor do Desconto (R$): ", precoDesconto)
    print("Preço total com 10% de desconto (R$): ", precoTotal)

elif(formaPagamento == "2"):
    precoDesconto = valorProduto * 0.05
    precoTotal = valorProduto - precoDesconto
    print("Valor do Produto (R$): ", valorProduto)
    print("Valor do Desconto (R$): ", precoDesconto)
    print("Preço total com 5% de desconto (R$): ", precoTotal)

elif(formaPagamento == "3"):
    print("Valor do Produto (R$): ", valorProduto)

elif (formaPagamento == "4"):
    precoTotal = valorProduto * 1.07
    precoAcrescimo = precoTotal - 100
    print("Valor do Produto (R$): ", valorProduto)
    print("Valor do Juros (R$): ", precoAcrescimo)
    print("Preço total com 7% de juros (R$): ", precoTotal)
else:
    print("Operação Inválida, refaça novamente a operação")
