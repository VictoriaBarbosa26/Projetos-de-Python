#Atividade 28
N= int(input("Digite o primeiro termo da P.A:"))

R = int(input("Digite a razão da P.A:"))

D= N + (10 - 1) * R

for cont in range(N,D+R,R):
    formula = N + R

    print("{}".format(cont), end= " --> ")
print('FIM')