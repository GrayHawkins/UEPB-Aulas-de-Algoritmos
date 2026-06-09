tentativas = 1
login = "kézia"
senha = "123"
entradaLogin = input("digite o login: ")
entradaSenha = input("digite a senha: ")

while tentativas < 3 and (entradaLogin != login or entradaSenha != senha):
    if entradaSenha != senha:
        print (f"Senha inválida. Tente novamente. Erros: {tentativas}/3 ")
    elif entradaLogin != login:
           print(f"login inválido. Tente novamente. Erros: {tentativas}/3")
    elif entradaLogin != login and entradaSenha != senha:
        print(f"login e senha inválidos. Tente novamente. Erros: {tentativas}/3")
    tentativas += 1
    entradaLogin = input("digite o login: ")
    entradaSenha = input("digite a senha: ")

    
print("senha correta")

    
