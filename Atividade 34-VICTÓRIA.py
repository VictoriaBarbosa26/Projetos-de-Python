#Atividade 34
SEX = str(input('Digite seu sexo [M/F]: ')).upper()
while SEX != 'M' and SEX != 'F':
    print('Você não digitou M ou F')
    SEX = str(input('Digite seu sexo [M/F]: ')).upper()
    if SEX == 'M':
        print("Seu sexo é MASCULINO!! FIM DA EXECUÇÃO DO PROGRAMA")
    elif SEX == 'F':
        print("Seu sexo é FEMININO!! FIM DA EXECUÇÃO DO PROGRAMA")
