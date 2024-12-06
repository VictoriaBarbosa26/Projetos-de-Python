#Atividade 37
num = soma = 0
quant = -1
while num != 999:
    quant += 1
    soma += num
    num = int(input("Digite um número [999 para FINALIZAR a execução]: "))
print("A SOMA dos números e de: {}".format(soma))
print("A quantidade de números DIGITADOS e de: {}".format(quant))