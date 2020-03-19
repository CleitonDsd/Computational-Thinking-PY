# O RM de um aluno da FIAP é composto por 5 dígitos. Sua tarefa é escrever um algoritmo que
# recebe um RM e retorna a somatória de todos os dígitos do RM. Por exemplo, suponha que
# o aluno tenha o RM 56395, seu algoritmo deverá imprimir como saída 28 = 5+6+3+9+5.
# Dica: realize várias divisões e restos de divisões por 10.


soma = 0

digito1 = int(input("Digite o 1° digito de seu RM: "))
soma = soma + digito1

digito2 = int(input("Digite o 2° digito de seu RM: "))
soma = soma + digito2

digito3 = int(input("Digite o 3° digito de seu RM: "))
soma = soma + digito3

digito4 = int(input("Digite o 4° digito de seu RM: "))
soma = soma + digito4

digito5 = int(input("Digite o 5° digito de seu RM: "))
soma = soma + digito5

print ("Somatório: ", digito1, " * ", digito2, " * ", digito3, " * ", digito4, " * ", digito5, " = ", soma)