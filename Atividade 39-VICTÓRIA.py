#Atividade 39
n = int(input("Digite um número: ")) 
cont = 1 
print("A tabuada de {} é:".format(n)) 
while cont<=10: 
    t=cont * n 
    print("{} X {} = {}".format(n,cont,t)) 
    cont+=1