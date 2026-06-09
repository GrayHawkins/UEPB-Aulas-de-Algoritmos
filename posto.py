litros = float(input("quantos litros foram vendidos? "))
comb = input("qual é o tipo de combustível? digite 'G' para gasolina ou 'A' para álcool: ")
if comb == "G":
    preco = float(litros*2.50)
    
    if litros > 20:
        total = preco - (preco * 0.06)
        print("o valor total a ser pago é:", total, "reais")
    
    else:
        total = preco - (preco * 0.04)
        print("o valor total a ser pago é:", total, "reais")
    
elif comb == "A":
    preco = float(litros*1.90)
    
    if litros > 20:
        total = preco - (preco * 0.05)
        print("o valor total a ser pago é:", total, "reais")
    
    else:
        total = preco - (preco * 0.03)
        
        print("o valor total a ser pago é:", total, "reais")