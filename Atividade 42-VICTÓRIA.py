#Atividade 42
quant = qm = qf = 0
cont = "S"
while cont == "S":
    sex = str(input("Digite seu sexo[M]/[F]:")).upper()
    if sex == "M":
        qm +=1
        cont = str(input("Quer continuar? [S/N]")).upper()
        print("-------------------------------------------------")
        
    elif sex == "F":
        qf +=1
        cont = str(input("Quer continuar? [S/N]")).upper()
        print("-------------------------------------------------")
    
quant = qm+qf    
mdm = qm/quant     
mdf = qf/quant

print ("A quantidade de HOMENS é:{}".format(qf))
print ("A quantidade de MULHERES é:{}".format(qm))
print ("A MÉDIA de HOMENS que trabalha nesta empresa é:{}".format(mdm))
print ("A MÉDIA de MULHERES que trabalha nesta empresa é:{}".format(mdf))