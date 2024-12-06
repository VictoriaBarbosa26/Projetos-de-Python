#ATIVIDADE DE NOTAS (H)
#JOÃO LUÍS E VICTÓRIA SJC
saldodisp= float(input("R$99999999999999999999999999"))
sacar=int(input("Digite o valor que deseja sacar:R$"))
total=sacar
ced=50
totced=0
while True:
    if total >=ced:
        total-=ced
        totced+=1
    else:
        if totced>0:
            print(f"o total de {totced} cédulas de R${ced}")
        if ced==100:
            ced=50
        elif ced==50:
            ced=20
        elif ced==20:
            ced=10
        elif ced==10:
            ced=10
        totced=0
        if total==0:
            break

print("SAQUE CONCLUÍDO COM SUCESSO!!!")
print ("SEU SALDO DÍSPONIVEL APÓS ESSE SAQUE E DE: R$99999999999")



