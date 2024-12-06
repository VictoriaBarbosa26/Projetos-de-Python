
#BEBÊ 0 á 4
#MIRIM  5 á 9
#INFANTIL B 10 á 14
#JUNIOR A 15 á 19
#SÊNIOR 20 á 25
#MASTER 26+
idade = int(input("digite a idade do nadador:"))

if idade>= 0 and idade <= 4:
    print("A idade {} anos se encaixa na categoria BEBÊ!".format(idade))

elif idade >= 5 and idade <= 9:
    print("A idade {} anos se encaixa na categoria MIRIM!".format(idade))

elif idade >= 10 and idade <= 14:
    print("A idade {} anos se encaixa na categoria INFANTIL !".format(idade))

elif idade >= 15 and idade <= 19:
    print("A idade {} anos se encaixa na categoria  JUNIOR!".format(idade))

elif idade >= 20 and idade <= 25:
    print("A idade {} anos se encaixa na categoria SÊNIOR!".format(idade))

elif idade >= 26:
    print("A idade {} anos se encaixa na categoria MASTER!".format(idade))

