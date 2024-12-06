#Atividade 10

v1 = float (input("Digite a velocidade do veículo:"))
multa =(v1-80)*7

if v1>=81:
    print("Você foi multado em: {}".format(multa))
elif v1 <=80:
    print("Você NÃO foi multado!!!")
