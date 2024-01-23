print("Bem Vindo")
print("--------------------------")

def validador_login(nickname, senha):
    if(nickname == "" or senha == ""):
        print("Preencha todos os camapos")
        return 0

    else:
        print("Campos preenchidos")
        return 1
    

nickname = input("Informe seu nickname: ")
senha = input("Infome a senha: ")

validador_login(nickname, senha)

