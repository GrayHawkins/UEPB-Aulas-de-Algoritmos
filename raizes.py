import math

valorA = float(input("insira o valor de a: "))

if valorA == 0:
    print("a equação não é do segundo grau.")

else:
    valorB = float(input("insira o valor de b: "))
    valorC = float(input("insira o valor de c: "))

    delta = math.pow (valorB,2) - (4*valorA*valorC)

    if delta < 0:
        print("a equação não possui raízes reais.")
        
    elif delta ==0:
        x1= float((-valorB + math.sqrt(delta)) / (2*valorA) )
        print("a raiz é:", x1)

    else:
        x1= float((-valorB + math.sqrt(delta)) / (2*valorA) )
        x2= float((-valorB - math.sqrt(delta)) / (2*valorA) )
        
        print("as raízes são:", x1, "e", x2)

