#Atividade 23

S = 0
N = 0
for cont in range (1,51,1):
    U = int(input("Digite um número:"))
    S = U + S
    if U %3==0: 
        N=N+1
print("Os Divisiveis por 3 são:{}".format(N))
print ("A soma é:{}!!!".format(S))