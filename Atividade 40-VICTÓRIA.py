#Atividade 40
somam = somaf = quant = qm = qf = 0
maiorm = 0
menorm = 9999
maiorf = 0
menorf = 9999
cont = "S"
while cont == "S":
    sex = int(input("Digite seu sexo[1-M]/[2-F]:"))
    if sex == 1:
        IDM = int(input("Digite sua idade:"))
        cont = str(input("Quer continuar? [S/N]")).upper()
        qm +=1
        somam += IDM
        print("-------------------------------------------------")
        
    elif sex == 2:
        IDF = int(input("Digite sua idade:"))
        cont = str(input("Quer continuar? [S/N]")).upper()
        qf +=1
        somaf += IDF
        print("-------------------------------------------------")
    elif cont != 'S' and cont != 'N':
        cont = str(input("Você digitou uma OPÇÃO INVÁLIDA!!! Quer continuar? [S/N]")).upper()
    
    if IDM > maiorm:
        maiorm = IDM
    elif IDM<menorm:
        menorm = IDM
        
    elif IDF > maiorf:
        maiorf = IDF
    elif IDF<menorf:
        menorf = IDF
        

mdm = somam/qm
mdf = somaf/qf
        
print ("A MÉDIA de idades MASCULINA é:{}".format(mdm))
print ("A MÉDIA de idades FEMININA é:{}".format(mdf))
print ("A MAIOR idade dos HOMENS é:{}".format(maiorm))
print ("A MENOR idade dos HOMENS é:{}".format(menorm))
print ("A MAIOR idade das MULHERES é:{}".format(maiorf))
print ("A MENOR idade das MULHERES é:{}".format(menorf))