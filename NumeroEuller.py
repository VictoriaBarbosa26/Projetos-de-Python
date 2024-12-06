#ATIVIDADE DO NUMERO EULLER (G)
#JOÃO LUÍS E VICTÓRIA SJC
def factorial(A):
    lista=[]
    teste=1
    while A>0:
        lista.append(A)
        A-=1
    for A in lista: 
        teste *= A
    return teste

A=0
list=[]
while A!=19:
    fac=1/factorial(A)
    list.append(fac)
    A+=1
    print("e = ",sum(list))
    print(A)
    