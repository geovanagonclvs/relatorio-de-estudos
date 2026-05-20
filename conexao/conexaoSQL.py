def conectar():

    import sqlite3

    conn = sqlite3.connect('relatorio.db')

    return conn
