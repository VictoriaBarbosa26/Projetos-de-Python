#Atividade 29
C = SPE = IE = SPC = IC = SPA = IA =0

for cont in range (1,501,1):
    C = int(input("Digite seu CURSO:[1-Engenharia] [2-Computação] [3-Administração]"))

    if C == 1:
        SPE = SPE+1
        CCE = print("O curso escolhido foi:ENGENHARIA")
        CE = int(input("Digite sua idade:"))
        if CE >=20 and CE<=25:
          IE =  IE+1
        else:
            print ("Não foi registrado este aluno pois não tem idade entre 20 e 25 anos!!!")
  

    elif C == 2:
        SPC = SPC+1
        CCC = print("O curso escolhido foi:COMPUTAÇÃO")
        CC = int(input("Digite sua idade:"))
        if CC >=20 and CC<=25:
          IC =  IC+1
        else:
            print ("Não foi registrado este aluno pois não tem idade entre 20 e 25 anos!!!")
   

    elif C == 3:
        SPA = SPA+1
        CCA = print("O curso escolhido foi:ADMINISTRAÇÃO")
        CA = int(input("Digite sua idade:"))
        if CA >=20 and CA<=25:
          IA =  IA+1
        else:
            print ("Não foi registrado este aluno pois não tem idade entre 20 e 25 anos!!!")

            
    else:
        print("OPÇÃO DE CURSO ESCOLHIDA INVÁLIDA!!!")
        
  
  
MDE= CE/SPE
MDC= CC/SPC
MDA= CA/SPA


if MDE<MDC and MDE<MDA:
    print ("O CURSO com menor idade média é ENGENHARIA!")

elif MDC<MDA and MDC<MDE:
    print ("O CURSO com menor idade média é COMPUTAÇÃO!")
    
elif MDA<MDE and MDA<MDC:
    print ("O CURSO com menor idade média é ADMINISTRAÇÃO!")
    
else:
    print ("Todos os CURSOS tem a mesma idade média!")
    
    
print("O número de alunos por curso de ENGENHARIA é:{}".format(SPE))
print("O número de alunos no curso de ENGENHARIA com idade entre 20 e 25 anos é:{}".format(IE))


print("O número de alunos por curso de COMPUTAÇÃO é:{}".format(SPC))
print("O número de alunos no curso de COMPUTAÇÃO com idade entre 20 e 25 anos é:{}".format(IC))


print("O número de alunos por curso de ADMINISTRAÇÃO é:{}".format(SPA))
print("O número de alunos no curso de ADMINISTRAÇÃO com idade entre 20 e 25 anos é:{}".format(IA))