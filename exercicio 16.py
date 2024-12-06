#Atividade 16
a1=int(input("Digite seu ano de nascimento:"))
a2=int(input("Digite o ano que estamos atualmente:"))
a3=a2-a1
a4=a3-18
if a3 == 18:
    print ("Aliste-se já!!! Está no tempo certo")
elif a3>18:
    print ("JÁ PASSOU DO TEMPO DE SE ALISTAR HEIN CAMPEÃO, já se passaram {} anos".format(a4))
else:
    print ("Ainda está cedo relaxe, e não deixe de se alistar quando estiver na idade certa,faltam {} anos!".format(a4))
