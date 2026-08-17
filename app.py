# do módulo flask, importamos os recursos do Flask
import sqlite3
from flask import Flask, render_template, request, redirect, url_for, jsonify, g
from tabela import  pegarDados, condicoes, salvar_conta, consultar_conta
from conexao.conexaoSQL import conectar
import re
import bcrypt


resposta = {"status": "sucesso"}

# criação do site + o nome dele.

app = Flask(__name__)

DATABASE = 'relatorio.db'

# define o endereço
# "/" significa a página inicial.
# se estivesse como "/relatorio", o texto só aparecia quando você digitasse localhost:5000/relatorio
@app.route("/", methods=["GET"])

#função responsável por dizer ao servidor o que fazer quando alguém visitar o endereço.
def home():
    
    return render_template("login.html", mostrar_tabela=False)


@app.route("/verificar", methods=["POST"])

def verificar_conta():

    conn = conectar()
    
    email = request.form.get("nemail")
    senha = request.form.get("nsenha")

    resultado = consultar_conta(conn, email, senha)

    if resultado == True:

        return render_template("dados.html")

    else:

        return render_template("login.html", resultado=resultado)
    

@app.route("/validar_pattern", methods=["GET"])

def validar_pattern():

    conn = conectar()
    
    email = request.form.get("nemail")
    senha = request.form.get("nsenha")
    
    pattern_email = r'^[a-zA-Z0-9]{4,}@[a-z]{5,}\.[a-z]{3,}$'
    pattern_senha = r'^[A-Za-z0-9@!]{6,}'
    
    resultado_email = re.match(pattern_email, email)
    
    resultado_senha = re.match(pattern_senha, senha)
    
    if resultado_email != None and resultado_senha != None:

        return redirect("/renderizar_pagina")

    
@app.route("/renderizar_pagina", methods=["GET"])

def renderizar_pagina():

    return render_template("criarconta.html")
    

@app.route("/criar_conta", methods = ["GET", "POST"])

def criar_conta():

    render_template("criarconta.html")

    conn = conectar()
        
    email = request.form.get("nemail")
    senha = request.form.get("nsenha")
    
    email_minusculo = email.lower()

    # transforma a string em um array de bytes
    senha_bytes = senha.encode('utf-8')

    # parêmetro rounds controla o custo computacional (padrão costumar ser 12)
    salt = bcrypt.gensalt(rounds=12)

    #recebe a senha e o salt, devolve o hash
    hashed = bcrypt.hashpw(senha_bytes, salt)

    # #compara uma senha em texto com um hash já existente
    # bcrypt.checkpw(senha, hash_salt)

    # retorna uma string em bytes contendo o hash seguro da senha combinado com o salt gerado.
    # hash_bytes = bcrypt.hashpw(hash_salt)

    return salvar_conta(conn, email_minusculo, hashed), render_template("dados.html")

    
@app.route("/enviar", methods=["POST"])

def enviar():

    conn = conectar()

   

    materia = request.form.get('textmateria')
    questoes = request.form.get('numberquestoes')
    questoesCertas = request.form.get("numbercertas")
    horas = request.form.get("horas")

    condicoes(int(questoes), int(questoesCertas))

    porcentagem = condicoes(int(questoes), int(questoesCertas))

    pegarDados(conn, materia, int(questoes), int(questoesCertas), float(horas), float(porcentagem))

    return render_template("mostrar.html")


def mostrar_relatorio():

    ...
  
# Com essa condição, o site só é executado se você rodar o app.py diretamente. 
# Se ele for importado pelo teste.py, o site não é exeutado.

if __name__ == "__main__":

    
    app.run(debug=True)