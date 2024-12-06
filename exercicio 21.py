
from random import randint
from time import sleep
itens = ('PEDRA','PAPEL','TESOURA')
computador = randint (0,2)
print ('''Suas opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
jogador = int(input ("Qual é a sua jogada?\n"))

if jogador == 0 or jogador == 1 or jogador == 2:
    print("JO")
    sleep(1)
    print("KEN")
    sleep(1)
    print("PO!!!")
    sleep(1)

    print('-=' * 12)
    print ("COMPUTADOR jogou:{}".format(itens[computador]))
    print("JOGADOR jogou:{}".format(itens[jogador]))
    print('-=' * 12)

    if computador == 0:
        if jogador == 0:
            print("EMPATE!!!")
        elif jogador == 1:
            print("JOGADOR VENCEU!!!")
        elif jogador == 2:
            print("COMPUTADOR VENCEU!!!")
        else:
            print("JOGADA INVÁLIDA")

    elif computador == 1:
        if jogador == 0:
            print ("COMPUTADOR VENCEU")
        elif jogador == 1:
            print("EMPATE!!!")
        elif jogador == 2:
            print("JOGADOR VENCEU!!!")
        else:
            print("JOGADA INVÁLIDA")

    elif computador == 2:
        if jogador == 0:
            print("JOGADOR VENCEU")
        elif jogador == 1:
            print("COMPUTADOR VENCEU!!!")
        elif jogador == 2:
            print("EMPATE!!!")
        else:
            print ("JOGADA INVÁLIDA")

else:
    print("OPÇÃO INVÁLIDA!!! TENTE NOVAMENTE")


