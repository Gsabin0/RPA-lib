import pyodbc


def con_banco(server, database,username,password):
    """
    Estabelece uma conexão com um banco de dados SQL Server e retorna um cursor.

    Args:
        server (str): O nome do servidor do banco de dados.
        database (str): O nome do banco de dados.
        username (str): O nome de usuário para autenticação no banco de dados.
        password (str): A senha para autenticação no banco de dados.

    Returns:
        pyodbc.Cursor: O cursor para executar consultas SQL no banco de dados.
    """
    try:
        server = server  
        database = database
        username = username
        password = password
        cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';ENCRYPT=no;UID='+username+';PWD='+ password)
        cursor = cnxn.cursor()
        print(f'Conexão com {server}, bem Sucedida!')
        return cursor
    except:
        print(f'Erro na conexão com {server}')


def select(con,tabela):
    """
    Executa uma consulta SELECT em uma tabela do banco de dados.

    Args:
        con (pyodbc.Cursor): O cursor da conexão com o banco de dados.
        tabela (str): O nome da tabela a ser consultada.

    Returns:
        list: Uma lista contendo as linhas resultantes da consulta SELECT.
    """
    s = con.execute(rf'SELECT * FROM {tabela}').fetchall()
    return s

