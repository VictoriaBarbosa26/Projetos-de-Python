#Atividade 26
SSM = SSF = QM = QF = 0
for cont in range (1,16,1):
    S = int(input("Digite seu Sexo [1-Masculino][2-Feminino]:"))
    if S == 1:
        SM = float(input("Digite seu sálario:"))
        SSM = SSM + SM
        QM = QM + 1
    
    elif S == 2:
        SF = float(input("Digite seu sálario:"))
        SSF = SF + SSF
        QF = QF + 1
        
    else:
        print("OPÇÃO ESCOLHIDA INVÁLIDA!!!")

MDF = SSF/QF
MDM = SSM/QM        

print("A média dos Sálarios Masculinos é:{}. E a quantidade de HOMENS que respoderam a pesquisa foi de: {} HOMENS".format(MDM,QM))
print("A média dos Sálarios Femininos é:{}. E a quantidade de MULHERES que respoderam a pesquisa foi de: {} MULHERES".format(MDF, QF))