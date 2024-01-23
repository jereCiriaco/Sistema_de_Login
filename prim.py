import os
from PySimpleGUI import PySimpleGUI as sg



def verifica_login(nickname, senha):
    if(nickname == "" or senha == ""):
        print("Preencha todos os camapos")
        return 0

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

#Layout 
sg.theme('Reddit')
layout = [
    [sg.Text("Usuario:"), sg.Input(key = "usuario", size=(25,1))],
    [sg.Text("Senha:  "), sg.Input(key="senha",size=(25,1),password_char="*")],
    [sg.Button("ENTER")], 
    [sg.Output(size=(50,5), key="output")]

]
#Janela
janela = sg.Window("Tela de Login", layout)

#Ler os eventos
while True:
    eventos, valores = janela.read()
    if eventos == sg.WINDOW_CLOSED:
        break
    if eventos == "ENTER":
        info = verifica_login(valores["usuario"],valores["senha"])
        if(info !=None):
            janela["output"].update(value=info)

        

