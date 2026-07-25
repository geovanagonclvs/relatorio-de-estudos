# do módulo flask, importamos os recursos do Flask
from flask import Flask, render_template, request, redirect, url_for, jsonify
from tabela import mostrar_relatorio, pegarDados, condicoes
from conexao.conexaoSQL import conectar

resposta = {"status": "sucesso"}

# criação do site + o nome dele.

app = Flask(__name__)

# define o endereço
# "/" significa a página inicial.
# se estivesse como "/relatorio", o texto só aparecia quando você digitasse localhost:5000/relatorio
@app.route("/")

#função responsável por dizer ao servidor o que fazer quando alguém visitar o endereço.
def home():


    return render_template("login.html", mostrar_tabela=False)


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

    mostrar_relatorio(conn)

    dados = mostrar_relatorio(conn)

    return render_template("index.html", mostrar_relatorio=False)
 

@app.route("/tabela", methods=["POST"])
def mostrar_table():

    conn = conectar()

    mostrar_relatorio(conn)

    dados = mostrar_relatorio(conn)

  
    return render_template("index.html", mostrar_tabela =True,  apelido=dados)

    
# Com essa condição, o site só é executado se você rodar o app.py diretamente. 
# Se ele for importado pelo teste.py, o site não é exeutado.

if __name__ == "__main__":

    
    app.run(debug=True)