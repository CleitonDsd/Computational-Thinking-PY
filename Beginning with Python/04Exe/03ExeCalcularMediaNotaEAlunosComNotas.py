# Altere o algoritmo anterior para, além da média, contar os alunos que tiraram entre 0 e 5,0
# (0 ≤ nota < 5, 0) e acima de 5, 0 (nota ≥ 5, 0).

quantidadeAlunos = int(input("Digite a quantidade de alunos: "))

contador = 0
soma = 0
media = 0
alunosRetidos = 0
alunosAprovados = 0
contadorAlunosAprovados = 0
contadorAlunosRetidos = 0

while(contador < quantidadeAlunos):
    contador = contador + 1
    print(contador , "° Aluno")
    nota = int(input("Nota: "))
    print("=======")
    if ((nota <= 0) or (nota <=5)):
        contadorAlunosRetidos = contadorAlunosRetidos + 1
        alunosRetidos = contadorAlunosRetidos

    elif(nota > 5 ):
        contadorAlunosAprovados = contadorAlunosAprovados + 1
        alunosAprovados = contadorAlunosAprovados

    soma = soma + nota
    media = soma / quantidadeAlunos

print("Média Final da Sala: ", media)
print("Total Alunos Retidos: ", alunosRetidos)
print("Total Alunos Aprovados: ", alunosAprovados)
