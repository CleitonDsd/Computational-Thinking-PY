# Escreva um algoritmo que recebe a idade de um nadador e mostra sua categoria conforme a
# tabela a seguir:
# Categoria Idade
# Infantil 5 a 7
# Juvenil 8 a 10
# Adolescente 11 a 15
# Adulto 16 a 30
# Senior acima de 30


idade = int(input("Digite a idade do Atleta: "))


if(idade < 0) or (idade < 5) or (idade >= 101):
    print("Sem modalidade para esta idade")

elif (idade >= 5) or (idade <=7):
    print("Categoria: Infantil | Idade: 5 a 7 anos")

elif(idade >= 8) or (idade <=10):
    print("Categoria: Juvenil | Idade: 8 a 10 anos")

elif(idade >= 11) or (idade <=15):

    print("Categoria: Adolescente | Idade: 11 a 15 anos")

elif(idade >= 16) or (idade <=30):
    print("Categoria: Adulto | Idade: 16 a 30 anos")

elif(idade >30):
    print("Categoria: Senior | Idade: acima de 30 anos")
