#Atividade 25
S = Q = N = 0
for cont in range (1,21,1):
	N=str(input('Digite seu nome: '))
	I=int(input('Digite sua idade: '))
	S = S + I
	Q = Q + 1
	MD = S/Q
print('a média das idades é: {}'.format(MD))