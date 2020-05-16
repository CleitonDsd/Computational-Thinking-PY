# Um vendedor recebe um salário xo de R$ 500,00 reais mais comissões sobre suas vendas.
# Porém o percentual das comissões são diferentes de acordo com a classicação dos produtos.
# Veja a tabela abaixo indicando a categoria e os respectivos percentuais.
# categoria descrição comissão (%)
# 1 camisetas e polos 4,0
# 2 calças e camisas 5,5
# 3 jaquetas e agasalhos 7,0
# 4 ternos e sobretudos 8,5
# Sua tarefa será a de escrever um algoritmo que calcula o salário mensal do funcionário.
# Observe que faz parte do exercício você denir as informações que serão fornecidas pelo
# usuário para o cálculo do salário.

salario = 500
salarioTotal = salario
categoria = 10

nome = input("Caro Colaborador, digite seu nome: ")
while (categoria != 0):

    categoria = int(input("Digite a Categoria do Produto: "))

    if categoria == 1:

        salario = salario * 0.04 + salario
        salarioTotal = salario

    elif categoria == 2:
        salario = salario * 0.55 + salario
        salarioTotal = salario

    elif categoria == 3:
        salario = salario * 0.07 + salario
        salarioTotal = salario

    elif categoria == 4:
        salario = salario * 0.85 + salario
        salarioTotal = salario

    elif categoria == 0:
        print("")
        print("Saindo do sistema - Contabilizando... ")
        print("")
    else:
        print("Operação inválida, tente novamente.")


print("")
print("==== Folha Salarial ===")
print("Colaborador: ", nome)
print("")
salario = 500
totalComissao = salarioTotal - salario
print("Salário Bruto(R$): ",salario)
print("Valor das comissões(R$): ",totalComissao)
print("Salário Total (R$): ",salarioTotal)
