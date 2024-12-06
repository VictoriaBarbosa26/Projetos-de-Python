#Atividade 43
soma = quant = 0
maior = 0
menor = 9999
cont = 'S'
while cont == 'S':
    peso = int(input('Digite o seu peso em KG: '))
    id = int(input('Digite sua idade: '))
    cont = str(input('Quer continuar? [S/N] ')).upper()
    print("--------------------------------------------")
    if cont != 'S' and cont != 'N':
        cont = str(input("Você digitou uma OPÇÃO INVÁLIDA!!! Quer continuar? [S/N]")).upper()
    
       
    soma += id
    quant += 1
    md = soma/quant  
    
    if peso > maior:
        maior = peso
    elif peso<menor:
        menor = peso

print ("A MÉDIA de idades é:{}".format(md))
print ("A pessoa que tem o MAIOR peso da cidade pesa:{}KG".format(maior))
print ("A pessoa que tem o MENOR peso da cidade pesa:{}KG".format(menor))
