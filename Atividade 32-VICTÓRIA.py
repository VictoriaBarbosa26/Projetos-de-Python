#Ativdade 32
N = int(input ("Digite um numero saber se ele e primo ou não:"))
I = 0

for cont in range(1,N+1):
    if N%cont == 0:
        I += 1
        
if I == 2:
    print ("O número é primo")
        
else:
    print ("O número NÃO é primo")