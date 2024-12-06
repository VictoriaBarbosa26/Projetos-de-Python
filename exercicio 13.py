#Atividade 13
s1= float(input("Digite seu salário:"))
s2=(s1*0.10)
s3=(s1*0.15)
if s1>1250:
    print ("Seu aumento é de:{}".format(s2))
else:
    print("Seu aumento é de:{}".format(s3))