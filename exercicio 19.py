#ABAIXO DO PESO 18,5
#PESO IDEAL 18,6 á 25
#SOBREPESO 26 á 30
#OBESIDADE 31 á 40
#OBESIDADE MÓRBIDA +40
altura = float(input("Digite sua Altura:"))
peso = float(input("Digite seu peso:"))
IMC = peso/(altura**2)


if IMC <18.5:
    print("Seu IMC é:{}! É você está ABAIXO do peso!".format(IMC))

elif IMC >= 18.6 and IMC <= 25:
    print("Seu IMC é:{}! É você está no peso IDEAL.".format(IMC))

elif IMC >= 26 and IMC <= 30:
    print("Seu IMC é:{}! É você está SOBREPESO!".format(IMC))

elif IMC >= 31 and IMC <= 40:
    print("Seu IMC é:{}! É você está com OBESIDADE!".format(IMC))

elif IMC > 40:
    print("Seu IMC é:{}! É você está com OBESIDADE MÓRBIDA!".format(IMC))
