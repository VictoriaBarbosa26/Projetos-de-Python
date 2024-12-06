#Atividade 41
perna = frajo = taz = pato = branco = 0
E = 1
while E !=0:
    print("SUAS OPÇÕES!")
    print ("[10] - Pernalonga")
    print ("[30] - Frajola")
    print ("[42] - Taz")
    print ("[55] - Patolino")
    print ("[1] - Branco")
    print ("[0] - Sair da Eleição")
    E=int(input("Escolha uma das opções acima: "))
    
    if E == 10:
        perna = perna+1
        print ("O candidato escolhido foi o PERNALONGA!!!")
        print("-------------------------------------------------")
        
    elif E == 30:
        frajo = frajo+1
        print ("O candidato escolhido foi o FRAJOLA!!!")
        print("-------------------------------------------------")
        
    elif E == 42:
        taz = taz+1
        print ("O candidato escolhido foi o TAZ!!!")
        print("-------------------------------------------------")
        
    elif E == 55:
        pato = pato+1
        print ("O candidato escolhido foi o PATOLINO!!!")
        print("-------------------------------------------------")
        
    elif E == 1:
        branco = branco+1
        print ("SEU VOTO FOI EM BRANCO!!!")
        print("-------------------------------------------------")
        
    elif E!=10 and E!=30 and E!=42 and E!=55 and E!=0 and E!=1:
        branco = branco+1
        print("Seu voto foi NULO!!!")
        print("-------------------------------------------------")
        
    elif E == 0:
        tot=perna+frajo+taz+pato+branco
        print ("FIM DAS ELEIÇÕES! VEJA OS RESULTADOS ABAIXO!!!")
        
        
if perna>frajo and perna>taz and perna>pato and perna>branco:
    print("O candidato que VENCEU as eleições foi o PERNALONGA!!!")
    print("Com {} votos!!!".format(perna))
    print("-------------------------------------------------")
    
if frajo>perna and frajo>taz and frajo>pato and frajo>branco:
    print("O candidato que VENCEU as eleições foi o FRAJOLA!!!")
    print("Com {} votos!!!".format(frajo))
    print("-------------------------------------------------")   
            
elif taz>perna and taz>frajo and taz>pato and taz>branco:
    print("O candidato que VENCEU as eleições foi o TAZ!!!")
    print("Com {} votos!!!".format(taz))
    print("-------------------------------------------------")
    
elif pato>perna and pato>frajo and pato>taz and pato>branco:
    print("O candidato que VENCEU as eleições foi o PATOLINO!!!")
    print("Com {} votos!!!".format(pato))
    print("-------------------------------------------------")
    
elif branco>perna and branco>frajo and branco>taz and branco>pato:
    print("NENHUM CANDIDATO VENCEU AS ELEIÇÕES, A MAIORIA DOS VOTOS FOI NULO!!!")
    print("Foram {} votos NULOS!!!".format(branco))
    print("-------------------------------------------------")
    
    
mdp=perna/tot
porp=perna*100/tot
mdf=frajo/tot
porf=frajo*100/tot
mdt=taz/tot
port=taz*100/tot
mdd=pato/tot
pord=pato*100/tot 
N=branco+branco
mdn=branco/tot
porn=branco*100/tot

print("A média de votos do PERNALONGA foi de: {} votos!!!".format(mdp))
print("A porcentagem de votos do PERNALONGA foi de: {}%!!!".format(porp))
print("-----------------------------------------------------------------")
print("A média de votos do FRAJOLA foi de: {} votos!!!".format(mdf))
print("A porcentagem de votos do FRAJOLA foi de: {}%!!!".format(porf))
print("-----------------------------------------------------------------")
print("A média de votos do TAZ foi de: {} votos!!!".format(mdt))
print("A porcentagem de votos do TAZ foi de: {}%!!!".format(port))
print("-----------------------------------------------------------------")
print("A média de votos do PATOLINO foi de: {} votos!!!".format(mdd))
print("A porcentagem de votos do PATOLINO foi de: {}%!!!".format(pord))
print("-----------------------------------------------------------------")
print("A média de votos NULOS foi de: {} votos!!!".format(mdn))
print("A porcentagem de votos NULOS foi de: {}%!!!".format(porn))
print("-----------------------------------------------------------------")
print("FIM DA EXECUÇÃO DO PROGRAMA!!!")