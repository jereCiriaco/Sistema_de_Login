import os

def validador_login(nickname, senha):
    if(nickname == "" or senha == ""):
        print("Preencha todos os camapos")
        return 0
    else:
        print("Campos preenchidos")
        return 1

def verifica_login(nickname):
    # Abre o arquivo em modo de leitura ('r')
    with open("banco_de_dados.txt", "r") as arquivo:
        # Lê cada linha do arquivo
        for linha in arquivo:
            # Imprime cada linha
            user =linha.strip().split(",")  # strip() remove espaços em branco extras no início e no final de cada linha
            print(user[0])

            if(user[0] == nickname):
                print("Usuario encontrado no Banco de dados")
                return user




os.system("cls")
print("Bem Vindo")
print("--------------------------")
nickname = input("Informe seu nickname: ")
senha = input("Infome a senha: ")
    

validador_login(nickname, senha)
ususario = verifica_login(nickname)
if(ususario):
    for info in ususario:
        print(info, end=" ")

