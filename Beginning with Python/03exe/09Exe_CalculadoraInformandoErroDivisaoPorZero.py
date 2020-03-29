# No exercício da calculadora, visto em sala de aula, temos um problema com a operação
# de divisão. Sua tarefa será exibir uma mensagem informando que é impossível fazer uma
# divisão por 0. Note que, essa mensagem só deverá aparecer quando o usuário quiser fazer
# tal operação.

valorA = float(input(": "))

print(" + | - | * | / ")
operacao = input()

if (operacao == "+" ):
    valorB = float(input(""))
    resultado = valorA + valorB
    print(" = ", resultado)

elif(operacao == "-" ):
    valorB = float(input(""))
    resultado = valorA - valorB
    print(" = ", resultado)

elif(operacao == "*" ):
    valorB = float(input(""))
    resultado = valorA * valorB
    print(" = ", resultado)

elif(operacao == "/" ):
    valorB = float(input(""))
    if(valorB == 0):
        print("Erro de operação, impossível dividir por 0")
        exit()
    resultado = valorA / valorB
    print(" = ", resultado)
else:
    print("Erro de semântica ou operação! Refaça a conta!")