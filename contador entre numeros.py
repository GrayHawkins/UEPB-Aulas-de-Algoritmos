numero = int(input("digite um número: "))
contador1 = 0
contador2 = 0
contador3 = 0
contador4 = 0
while numero >= 0:
    if numero  >= 0 and numero<=25:
        contador1 += 1
        print (f"números entre 0 e 25: {contador1}")
    elif numero  > 25 and numero <=50:
        contador2 += 1
        print(f"números entre 26 e 50: {contador2}")
    elif numero  > 50 and numero <= 75:
        contador3 += 1
        print (f"números entre 51 e 75: {contador3}")
    
    elif numero  > 75 and numero <= 100:
        contador4 += 1
        print (f"números entre 76 e 100: {contador4}")

    numero = int(input("digite um número: "))
if numero < 0:
    print("número inválido")