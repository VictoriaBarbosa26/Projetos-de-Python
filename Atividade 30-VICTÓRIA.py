#Atividade 30

QSALF = SSF  = QSALM = SSM = 0
MAIDF = 0
MEIDF = 9999
MAIDM = 0
MEIDM = 9999
HA = int(input("Digite o número de Habitantes:"))

for cont in range (1,HA+1):
    SEX = int(input("Digite seu sexo:[1-MASCULINO]/[2-FEMININO]"))
    if SEX == 2:
        QSALF = QSALF+1
        SALF =  float(input("Digite seu sálario:"))
        SSF = SSF + SALF
        IDF = int(input("Digite sua idade:"))
        if IDF > MAIDF:
            MAIDF = IDF
        else:
            MEIDF = IDF
            
    elif SEX == 1:
        QSALM = QSALM+1
        SALM =  float(input("Digite seu sálario:"))
        SSM = SSM + SALM
        IDM = int(input("Digite sua idade:"))
        if IDM > MAIDM:
            MAIDM = IDM
        else:
            MEIDM = IDM
            
    else:
        print("SEXO INVÁLIDO!!! TENTE NOVAMENTE!!!")
        
MSALF = SSF/QSALF
MSALM = SSM/QSALM
MSAL = (SSF + SSM) / 2

print ("A média de sálario desse grupo é:{}".format(MSAL))
print ("A média de sálario FEMININO é:{}".format (MSALF))
print ("A média de sálario MASCULINO é:{}".format (MSALM))
print ("A MAIOR idade do grupo FEMININO é:{}".format (MAIDF))
print ("A MENOR idade do grupo FEMININO é:{}".format (MEIDF))
print ("A MAIOR idade do grupo MASCULINO é:{}".format (MAIDM))
print ("A MENOR idade do grupo MASCULINO é:{}".format (MEIDM))