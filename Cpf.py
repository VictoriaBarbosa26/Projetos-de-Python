#ATIVIDADE DO CPF (J)
#JOÃO LUÍS E VICTÓRIA SJC
from random import randint

def cpf_validate(numbers):

    cpf = [int(char) for char in numbers if char.isdigit()]

    if len(cpf) != 11:
        return False

    
    if cpf == cpf[::-1]:
        return False
  
    for cont in range(9, 11):
        value = sum((cpf[numero] * ((cont+1) - numero) for numero in range(0, cont)))
        digite = ((value * 10) % 11) % 10
        if digite != cpf[cont]:
            return False
    return True

def cpf_generate():
    while True:
        cpf = [randint(0, 9) for cont in range(9)]
        if cpf != cpf[::-1]:
            break

    for cont in range(9, 11):
        value = sum((cpf[numero] * ((cont + 1) - numero) for numero in range(0, cont)))
        digite = ((value * 10) % 11) % 10
        cpf.append(digite)

    resultado = ''.join(map(str, cpf))
    return resultado

tenta = int(input('''[1] VALIDE SEU CPF
[2] GERAR UM CPF VÁLIDO
[0]SAIR (FIM DO PROGRAMA)
OPÇÃO: '''))
if tenta == 1:
    cpf = input('DIGITE O CPF: ')
    if cpf_validate(cpf):
        print('CPF VÁLIDO!!!')
    else:
        print('CPF INVÁLIDO!!!')
elif tenta == 2:
    cpf = cpf_generate()
    if cpf_validate(cpf):
        print(f'O CPF GERADO FOI: {cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}')
elif tenta == 0:
    print('FIM DO PROGRAMA!!!')