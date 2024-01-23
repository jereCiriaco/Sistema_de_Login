import os
from PySimpleGUI import PySimpleGUI as sg

def verifica_login(nickname, senha):
    if nickname == "" or senha == "":
        return "Preencha todos os campos"
    # Abre o arquivo em modo de leitura ('r')
    with open("banco_de_dados.txt", "r") as arquivo:
        # Lê cada linha do arquivo
        for linha in arquivo:
            # Imprime cada linha
            user = linha.strip().split(",")  # strip() remove espaços em branco extras no início e no final de cada linha
            if user[0] == nickname:
                return f"Usuario encontrado no Banco de dados: {user[0],user[1]}"


def login(layout):
    # Janela
    janela = sg.Window("Tela de Login", layout)
    # Ler os eventos
    while True:
        eventos, valores = janela.read()
        if eventos == sg.WINDOW_CLOSED:
            break
        if eventos == "LOGAR":
            info = verifica_login(valores["usuario"], valores["senha"])
            if info:
                janela["info"].update(value="Logado com Sucesso")
            else:
                janela["info"].update(value="Usuario nao Cadastrado")


os.system("cls")
sg.theme('Reddit')
layout = [
        [sg.Text("Usuario:"), sg.Input(key="usuario", size=(25, 1))],
        [sg.Text("Senha:  "), sg.Input(key="senha", size=(25, 1), password_char="*")],
        [
            sg.Column(
                layout=[
                    [sg.Button("LOGAR")],
                    [sg.Button("CADASTRAR-SE")],
                    [sg.Text("", key="info", justification='center')]
                ],
                justification='center',
                element_justification='center',
                expand_x=True
            )
        ],
        
    ]
login(layout)



