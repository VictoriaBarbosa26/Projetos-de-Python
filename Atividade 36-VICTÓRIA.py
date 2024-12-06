#Atividade 36
cont = f = 1

n = float(input("Digite um número:"))
while cont <=n:
    
    f = f*cont
    cont +=1
    print("O fatorial de {} é:  {}".format(n,f))