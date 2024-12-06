p1 = float (input("Preço das compras:"))
print('''Formas de pagamento
[ 1 ] Á vista dinheiro/cheque
[ 2 ] Á vista cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão''')
opção = int (input ("Qual é a opçãp escolhida?"))
if opção == 1:
    t1 = p1 - (p1*0.1)
    print("Sua opção foi a {}ª e seu desconto foi de 10%,totalizando {}".format(1 ,t1))
elif opção == 2:
    t2 = p1 - (p1 * 0.05)
    print("Sua opção foi {}ª e seu desconto foi de 5%,totalizando {}".format(2,t2))
elif opção == 3:
    t3 = p1
    print("Sua opção foi {}ª e voc~e não obteve desconto, totalizando sua compra deu:".format(3,t3))
elif opção == 4:
    t4 = p1 + (p1 * 0.20)
    print("Sua opção foi {}ª e você não obteve desconto e pagara juros de 20%,totalizando {}".format(4,t4))
