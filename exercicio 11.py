#Atividade 11

d1= float(input("Digite a distância da viagem em KM:"))
d2=0.50*d1
d3=0.45*d1
if d1<=200:
    print("O preço da passagem e de:{}".format(d2))
elif d1 > 200:
        print("O preço da passagem e de:{}".format(d3))