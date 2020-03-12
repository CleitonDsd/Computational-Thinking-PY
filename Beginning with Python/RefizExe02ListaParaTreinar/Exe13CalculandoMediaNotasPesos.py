# Uma disciplina da faculdade possui 3 tipos de avaliações: NAC, AM e PS. A média da
# disciplina é calculada de forma ponderada, onde a NAC tem peso 2, o AM peso 3 e a PS
# peso 5. Escreva um algoritmo que calcula a média da disciplina, seu algoritmo deverá receber
# as três notas (NAC, AM e PS) e deverá imprimir o valor da média.
# MEDIA = (2  NAC + 3  AM + 5  PS)=10

nac = float(input("NAC, nota: "))
nac = nac * 2

am = float(input("AM, nota: "))
am = am * 3

ps = float(input("PS, nota: "))
ps = ps * 5

media = (nac + am + ps)/10

print ("===== Notas(*pesos) e Média =====")
print("NAC: ", nac)
print("AM: ", nac)
print("PS: ", ps)
print("Média: ", media)