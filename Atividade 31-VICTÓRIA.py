#Atividade 31
PBG = 0
PBM = 999999999
for cont in range (1,91):
    
    C = int (input("Digite o Número de indentificação do BOI:"))
    N=float(input("Digite o peso do BOI em KG:"))
    print ("-----------------------------------------------")
    
    if N > PBG:
        PBG = N
        gordo = C
    
    elif N<PBM:
        PBM = N
        magro = C
        
print("O BOI com MENOR peso pesa {}KG e seu número de indentificação é{}.".format(PBM,magro))
print("O BOI com MAIOR peso pesa {}KG e seu número de indentificação é{}.".format(PBG,gordo))
