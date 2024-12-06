#Atividade 38
soma = quant = 0
maior = 0
menor = 9999
cont = 'S'
while cont == 'S':
    num = int(input('Digite um número: '))
    cont = str(input('Quer continuar? [S/N] ')).upper()
    if cont != 'S' and cont != 'N':
        cont = str(input("Você digitou uma OPÇÃO INVÁLIDA!!! Quer continuar? [S/N]")).upper()
    
       
    soma += num
    quant += 1
    md = soma/quant  
    
    if num > maior:
        maior = num
    elif num<menor:
        menor = num

print ("A MÉDIA desses números é:{}".format(md))
print ("O MAIOR dentre esses números é:{}".format(maior))
print ("O MENOR dentre esses números é:{}".format(menor))
