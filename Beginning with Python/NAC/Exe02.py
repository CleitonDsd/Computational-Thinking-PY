# Exe02



salarioBase = 0
horaAtividade = 0
# descanso semanal remunerado coresponde a 1/6 do salário
dsr = 0



aulasSemanais = int(input("Digite o número de aulas semanais: "))
valorHoraAula = int(input("Digite o valor hora-aula (R$): "))
print("")
# Para calcular o salário base multiplicamos o número de aulas semanais por 4,5 semanas e pelo
# valor hora-aula

salarioBase = aulasSemanais * 4.5 * valorHoraAula
print("Salário Base (R$): ", salarioBase)

# o descanso semanal remunerado corresponde a 1/6 do salário base
dsr = salarioBase * 1/6
print("DSR (R$): ", dsr)

# a horaatividade corresponde a 5% da soma do salário base com o descanso semanal remunerado.
somandoParaObterHoraAtividade = salarioBase + dsr
horaAtividade = somandoParaObterHoraAtividade * 0.05
print("Hora Atividade (R$): ", horaAtividade)

print("")
salarioMensal = salarioBase + dsr + horaAtividade
print("Salário Mensal (R$): ", salarioMensal)