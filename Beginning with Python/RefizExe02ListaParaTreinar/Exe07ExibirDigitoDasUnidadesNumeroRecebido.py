# Sua tarefa é desenvolver um algoritmo que recebe um número inteiro de 0 a 99 e imprime o
# dígito das dezenas e o dígito das unidades desse número. Dica: usando papel e lápis faça a
# divisão inteira do número por 10 mas não coloque vírgula e nem acrescente 0 na divisão.


numero = int(input("Digite um número (0-99): "))

exibirUnidade = numero / 10

print("Número separado por digítos: ", exibirUnidade)

