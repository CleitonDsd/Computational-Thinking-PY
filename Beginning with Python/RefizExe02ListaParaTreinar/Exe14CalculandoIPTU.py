# As casas de São Paulo estão recebendo o carnê do IPTU com duas opções de pagamento:
# à vista ou em 10 vezes. Sua tarefa é desenvolver um programa/algoritmo onde o usuário
# informa (digita) o valor total à vista e o valor de cada parcela. Seu programa imprime o
# desconto em percentual dado pela prefeitura para pagamento à vista.

# 4% IPTU Á VISTA EM SP

valor = float(input("Digite o valor do IPTU (R$):" ))

porcentagem = 4

calcularDesconto = (valor * 4 )/100



print ("Valor do desconto (R$):", calcularDesconto)
print ("Valor total (R$):", valor - calcularDesconto)
