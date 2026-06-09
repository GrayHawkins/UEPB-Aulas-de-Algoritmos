p1 = input("1 - Telefonou para a vítima? \n╚═ ").lower()
p2 = input("\n2 - Esteve no local do crime? \n╚═ ").lower()
p3 = input("\n3 - Mora perto da vítima? \n╚═ ").lower()
p4 = input("\n4 - Devia para a vítima? \n╚═ ").lower()
p5 = input("\n5 - Já trabalhou com a vítima? \n╚═ ").lower()

respostas = [p1, p2, p3, p4, p5]

quantidade = 0

for resposta in respostas:
    if resposta.startswith("s"):
        quantidade += 1
        
if quantidade == 2:
    resultado = "Suspeito"
elif quantidade == 3 or quantidade == 4:
    resultado = "Cúmplice"
elif quantidade == 5:
    resultado = "Assassino"
else:
    resultado = "Inocente"

largura = 30

print("\n╚RESULTADO:")
print("╔" + "═" * largura + "╗")
print("║" + resultado.center(largura) + "║")
print("╚" + "═" * largura + "╝")