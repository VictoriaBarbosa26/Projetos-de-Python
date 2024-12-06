#Atividade 35
n1= float(input("Digite um número: "))
n2= float(input("Digite um número: "))
E = 0
while E !=6:
    print("SUAS OPÇÕES!")
    print ("[1] - Soma")
    print ("[2] - Multiplicar")
    print ("[3] - Subtrair")
    print ("[4] - Maior")
    print ("[5] - Novos Números")
    print ("[6] - Sair")
    E=int(input("Escolha uma das opções acima: "))
    
    if E == 1:
        n3 = n1+n2
        print ("O valor da soma desses números é:{}".format(n3))
        print("-------------------------------------------------")
        
    elif E == 2:
        n4 = n1*n2
        print ("O valor da multiplicação desses números é:{}".format(n4))
        print("-------------------------------------------------")
        
    elif E == 3:
        n5 = n1-n2
        print ("O valor da subtração desses números é:{}".format(n5))
        print("-------------------------------------------------")
        
    elif E == 4:
        if n1>n2:
            print ("O maior dentre esses números é:{}".format(n1))
        elif n2>n1:
            print ("O maior dentre esses números é:{}".format(n2))
            print("-------------------------------------------------")
            
    elif E == 5:
        nv1 = float(input("Digite o seu novo número: "))
        nv2 = float(input("Digite o seu novo número: "))
        print ("[1] - Soma")
        print ("[2] - Multiplicar")
        print ("[3] - Subtrair")
        print ("[4] - Maior")
        print ("[5] - Novos Números")
        print ("[6] - Sair")
        E=int(input("Escolha uma das opções acima: "))
        
        if E == 1:
            n5 = nv1+nv2
            print ("O valor da soma desses números é:{}".format(n5))
            print("-------------------------------------------------")
            
        elif E == 2:
            n6 = nv1*nv2
            print ("O valor da multiplicação desses números é:{}".format(n6))
            print("-------------------------------------------------")
            
        elif E == 3:
            n7 = nv1-nv2
            print ("O valor da subtração desses números é:{}".format(n7))
            print("-------------------------------------------------")
            
        elif E == 4:
            if nv1>nv2:
                print ("O maior dentre esses números é:{}".format(nV1))
                print("-------------------------------------------------")
                
            elif nv2>nv1:
                print ("O maior dentre esses números é:{}".format(nV2))
                print("-------------------------------------------------")
                
    elif E ==6:
        print("FIM DA EXECUÇÃO!!!")
            
    elif E > 6:
        print("OPÇÃO ESCOLHIDA INVÁLIDA! TENTE NOVAMENTE")
                
