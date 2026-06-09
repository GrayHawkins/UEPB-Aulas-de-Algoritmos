
loop=3
while loop >0:
    numero = int(input("insira um número: "))
    if numero >=0:
        print("o número é positivo.")
    else:
        print("o número é negativo.")
    loop-=1

    numeros =[numero]
    for numero in numeros:
        print(numero)
