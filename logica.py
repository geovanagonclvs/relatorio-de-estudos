from datetime import datetime
import re, bcrypt
from conexao.conexaoSQL import conectar
# def pegarValores():
    
#     try:

#         materia = input("Qual é a matéria estudada? ").strip().lower()
#         questoes = int(input("Total de questões de hoje: "))
#         questoesCertas = int(input("Quantas questões certas você resolveu?"))
#         horasEstudadas = float(input("Quantas horas você estudou hoje?"))

#         # retornar as variáveis que serão utilizadas nas outras funções
#         return materia, questoes, questoesCertas, horasEstudadas
    

#     except ValueError:
#         print("Digite um número válido!")

#         # retorna nada se o usário digitar algum número válido.     
#         return None, None, None, None
    

def condicoes(questoes, questoesCertas):

    if questoes <= 0:
        print("Não é possível dividir por 0!")
        return 0
    
    porcentagemConta = (questoesCertas / questoes) * 100
    porcentagem = round(porcentagemConta)

    if porcentagem >= 80:
        print ("Parabéns! VOcê está dominando muito bem essa matéria")
    elif 50 <= porcentagem <80:
        print("Você está indo bem, mas mas pode melhorar! :)")

    else:
        print("Cuidado! Estude mais essa matéria.")

    # Função retorna apenas o valor da variável porcentagem
    return porcentagem


def funcaoRelatorio (materia, horasEstudadas, porcentagem, questoes, questoesCertas):

    print(f""" 
-- Relatório de Estudos --
          
Matéria estudada: {materia}
Horas estudadas: {horasEstudadas}
Produtividade: {porcentagem}%
""")
    
   
    relatorio = (
        f"Matéria: {materia}; "
        f"Questões: {questoes}; "
        f"Certas: {questoesCertas}; "
        f"Horas : {horasEstudadas}; "
        f"Produtividade: {porcentagem}%; "
        #f"Data: {horarioFormatado}\n "
        

    )

    # Função retorna apenas o valor presente na variável relatorio
    return relatorio


# def salvarEmDocumento(materia, questoes, questoesCertas, horasEstudadas, porcentagem, arquivo="relatorioEstudos.csv"):

 
#     # Importamos o módulo os. Ele é últil para manipulação de dados e interação com o sistema operacional.
#     import os

#     #horarioFormatado = horario.strftime("%d/%m/%Y %H:%M")

#     horario = datetime.now()
#     horarioFormatado = horario.strftime("%d/%m/%Y %H:%M")

#     cabecalho = "materia,questoes,certas,horas,porcentagem,data"

    # # Abrir o arquivo no modo leitura
    # with open (arquivo, 'r') as f:

    #     #Se a variável cabecalho estiver no arquivo
    #     if cabecalho in f.read():
    #         with open(arquivo, 'a') as f:
    #             f.write(f"{materia},{questoes},{questoesCertas},{horasEstudadas},{porcentagem},{horarioFormatado}\n")


    #     # Se não estiver
    #     else:
    #         with open(arquivo, "w") as f:
    #             # Cabeçalho
    #             f.write("materia,questoes,certas,horas,porcentagem,data\n")
    #             f.write(f"{materia},{questoes},{questoesCertas},{horasEstudadas},{porcentagem},{horarioFormatado}\n")
   

def teste(conn, email, senha):

    cursor = conn.cursor()
     # cursor.execute("SELECT email, senha FROM usuarios WHERE email = ?", (email,))
    
    cursor.execute("SELECT email FROM usuarios WHERE email = ?", (email,))
 
    email_existir = cursor.fetchone()
 
    #se o email NÃO for igual ao do encontrado no fetchone
    if email_existir == None : 
 
           conta = (email, senha)
           sql = "INSERT INTO usuarios (email, senha) VALUES (?, ?)"
           cursor.execute(sql, conta)
           conn.commit()

           email_existir = False

           return print(email_existir)
 
     #se for igual, então:
    else:
 
         email_existir = True
         return print(email_existir )


conn = conectar()
teste(conn, "maria@gmail.com", "231231231")
