import mysql.connector

def validar_db(email, senha):
    conexao = mysql.connector.connect(
        host='localhost',
        database='users_db',
        user='root',
        password=''
    )

    try:
        if conexao.is_connected():
            print("Conectado ao Banco de Dados")
            cursor = conexao.cursor()

        cursor.execute('SELECT * FROM usuarios;')

        # Utilize fetchall() para obter todas as linhas da consulta
        linhas = cursor.fetchall()

        for linha in linhas:
            print(linha)
            if linha[2] == email and linha[3] == senha:
                return linha

    except mysql.connector.Error as err:
        print(f"Erro ao conectar ao banco de dados: {err}")

    finally:
        if conexao.is_connected():
            conexao.close()
            cursor.close()

    return None
