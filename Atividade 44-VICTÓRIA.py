#Atividade 44
thor = avengers = outro = minions= 0
E = 1
while E==1 or E==2 or E==3 or E==4:
    print("ESCOLHA A SESSÃO QUE DESEJA ASSISTIR O FILME!")
    print ("Sala [1]- Thor: Amor e Trovão")
    print ("Sala [2]- Avengers")
    print ("Sala [3]- O outro eu")
    print ("Sala [4]- Minions 2")
    E=int(input("Escolha uma das opções acima: "))
    
    if E == 1:
        thor+=1
        print ("O filme escolhido foi THOR: AMOR E TROVÃO!!!")
        print("-------------------------------------------------")
        
    elif E == 2:
        avengers+=1
        print ("O filme escolhido foi AVENGERS!!!")
        print("-------------------------------------------------")
        
    elif E == 3:
        outro+=1
        print ("O filme escolhido foi O OUTRO EU!!!")
        print("-------------------------------------------------")
        
    elif E == 4:
        minions+=1
        print ("O filme escolhido foi MINIONS 2!!!")
        print("-------------------------------------------------")
        
if E!=1 and E!=2 and E!=3 and E!=4:
    ("FIM DA EXECUÇÃO DO PROGRAMA!!!!")
        
        
total=thor+avengers+outro+minions        
mdg=total/4
pt=thor*100/total
pa=avengers*100/total
po=outro*100/total
pm=minions*100/total 


print("A quantidade de pessoas no CINEMA nesse dia eram de:{} pessoas".format(total))
print("A média GERAL de pessoas no cinema naquele dia são de:{} pessoas".format(mdg))
print("----------------------------------------------------------------------------")

print("A quantidade de pessoas que compraram ingresso para assistir THOR são de: {} pessoas".format(thor))
print("A porcentagem de pessoas na sala 1 são de: {}%!!!".format(pt))
print("-----------------------------------------------------------------")

print("A quantidade de pessoas que compraram ingresso para assistir AVENGERS são: {} pessoas".format(avengers))
print("A porcentagem de pessoas na sala 2 são de: {}%!!!".format(pa))
print("-----------------------------------------------------------------")

print("A quantidade de pessoas que compraram ingresso para assistir O OUTRO EU são: {} pessoas".format(outro))
print("A porcentagem de pessoas na sala 3 são de: {}%!!!".format(po))
print("-----------------------------------------------------------------")

print("A quantidade de pessoas que compraram ingresso para assistir MINIONS 2 são: {} pessoas".format(minions))
print("A porcentagem de pessoas na sala 4 são de: {}%!!!".format(pm))
print("-----------------------------------------------------------------")