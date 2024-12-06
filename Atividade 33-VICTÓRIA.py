#Atividade 33
from datetime import date
HJ = date.today().year
MA = 0
MN = 0
for cont in range(1,8,1):
    N = int(input("Digite seu ANO de nascimento:"))
    if HJ - N >= 19:
        MA += 1
    elif HJ - N < 18:
        MN += 1
print("São um total de {} pessoas MAIORES de idade".format(MA))
print("São um total de {} pessoas MENORES de idade".format(MN))