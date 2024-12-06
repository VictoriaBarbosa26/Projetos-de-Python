a1=float(input("Digite o tamanho do 1º lado do triângulo:"))
a2=float(input("Digite o tamanho do 2º lado do triângulo:"))
a3=float(input("Digite o tamanho do 3º lado do triângulo:"))
if a1 == a2 == a3:
    print ("É um triângulo EQUILÁTERO,pois todos os lados são iguais!!!")
elif a1 == a2 != a3:
    print("É um triângulo ISÓCELES, pois existem dois lados iguais e um diferente!!!")
elif a1 == a3 != a2:
    print("É um triângulo ISÓCELES, pois existem dois lados iguais e um diferente!!!")
elif a2 == a1 != a3:
    print("É um triângulo ISÓCELES, pois existem dois lados iguais e um diferente!!!")
elif a2 == a3 != a1:
    print("É um triângulo ISÓCELES, pois existem dois lados iguais e um diferente!!!")
elif a3 == a2 != a1:
    print("É um triângulo ISÓCELES, pois existem dois lados iguais e um diferente!!!")
elif a3 == a1 != a2:
    print("É um triângulo ISÓCELES, pois existem dois lados iguais e um diferente!!!")
elif a1 != a2 != a3:
    print ("É um triângulo ESCALENO, pois todos os lados são diferentes!!!")
