# Dados o número n de alunos de uma turma de Algoritmos e suas notas da primeira prova,
# determinar a média das notas dessa turma. Considere que o usuário digite as informações
# corretamente.

quantidadeAlunos = int(input("Digite a quantidade de alunos: "))

contador = 0
soma = 0
media = 0
while(contador < quantidadeAlunos):
    contador = contador + 1
    print(contador , "° Aluno")
    nota = int(input("Nota: "))
    print("=======")

    soma = soma + nota
    media = soma / quantidadeAlunos
print("Média Final da Sala: ", media)
