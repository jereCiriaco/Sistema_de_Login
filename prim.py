import PySimpleGUI as sg
from conectar import validar_db

def login(layout):
    # Janela
    janela = sg.Window("Tela de Login", layout)

    # Ler os eventos
    while True:
        eventos, valores = janela.read()
        if eventos == sg.WINDOW_CLOSED:
            break
        if eventos == "LOGAR":
            info = validar_db(valores["usuario"], valores["senha"])
            if info:
                janela["info"].update(value="Logado com Sucesso")
            else:
                janela["info"].update(value="Usuario nao Cadastrado")

    janela.close()

sg.theme('Reddit')
layout = [
    [sg.Text("Email:"), sg.Input(key="usuario", size=(25, 1))],
    [sg.Text("Senha: "), sg.Input(key="senha", size=(25, 1), password_char="*")],
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
