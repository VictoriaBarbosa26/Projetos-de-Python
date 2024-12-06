#Atividade 24

SP = QP = SN = QN = 0
for cont in range (1,41,1):
    N = float(input("Digite um número:"))
    if N>0: 
        SP=N+SP
        QP=QP+1
    else:
        SN= N+SP
        QN=QN+1
MP = SP/QP
MN = SN/QN
print ("A soma dos números POSITIVOS é:{}".format(SP))
print ("A quantidade dos números POSITIVOS é:{}".format(QP))
print ("A média dos números POSITIVOS é:{}".format(MP))
print ("A soma dos números NEGATIVOS é:{}".format(SN))
print ("A quantidade dos números NEGATIVOS é:{}".format(QN))
print ("A média dos números NEGATIVOS é:{}".format(MN))