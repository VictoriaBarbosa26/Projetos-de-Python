#Atividade 14
s1= float(input("Digite seu salário:"))
c1= float(input("Digite o valor da casa:"))
a1= int(input("Em quantos anos pretende pagar a casa?:"))
meses= a1*12
prestacao= c1 / meses
if prestacao > s1*0.3:
    print("Seu empréstimo foi NEGADO!!!")
else:
    print("Parabéns seu Empréstimo foi aprovado!!!")