# 5. A jornada de trabalho diária de um trabalhador é de 8 horas. Caso o trabalhador tenha
# trabalhado além da jornada mensal exigida, ele terá direito a receber hora-extra. O valor
# da hora-extra é o valor que ele recebe por hora acrescido de 50%. Supondo que ele trabalhe
# apenas nos dias úteis, escreva um algoritmo que recebe:
# a) o total de dias úteis de um mês
# b) o total de horas trabalhadas pelo trabalhador
# c) quanto o trabalhador recebe por hora
# Calcula e mostra o valor recebido a título de hora-extra (se houver) e o salário nal do
# trabalhador.

diasUteis = int(input("Dias úteis: "))
horasTrabalhadas = int(input("Horas Trabalhadas: "))
valorHoras = float(input("Valor Hora (R$): "))

calcularHoraPorDiasTrabalhados = 8 * diasUteis
horaExtra = valorHoras * 1.5

if (horasTrabalhadas > calcularHoraPorDiasTrabalhados):
    salarioTotal = horasTrabalhadas * horaExtra
    print("Salário total (R$): ", salarioTotal )

    valorHoraExtra = horasTrabalhadas - horaExtra
    print("Hora Extra (R$): ", valorHoraExtra)

    salarioBruto = salarioTotal - valorHoraExtra
    print("Salário Bruto (R$): ", salarioBruto)

else:
    salarioTotal = calcularHoraPorDiasTrabalhados * valorHoras
    print("Salário total (R$): ", salarioTotal)
    print("Hora Extra (R$): 0")
