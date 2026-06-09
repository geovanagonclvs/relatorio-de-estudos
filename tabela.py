from conexao.conexaoSQL import conectar


def criar_tabela(conn):

    

    cursor = conn.cursor()

    

    cursor.execute("""CREATE TABLE IF NOT EXISTS  relatorio(
                   
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   materia TEXT ,
                   questoes INTEGER NOT NULL,
                   questoesCertas INTEGER NOT NULL,
                   horas REAL NOT NULL,
                   porcentagem REAL NOT NULL
                   
                   )
                   

"""
    )

    cursor.execute("""CREATE TABLE IF NOT EXISTS usuarios(
                   
                   id_usuarios INTEGER PRIMARY KEY AUTOINCREMENT,
                   email TEXT UNIQUE,
                   senha TEXT
                   )




""")

    
   
    

    
    conn.commit()
    
    

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


def pegarDados(conn, materia, questoes, questoesCertas, horas, porcentagem, arquivo = "relatorio.db"):


    cursor = conn.cursor()

    cursor.execute("SELECT questoes, questoesCertas, horas, porcentagem FROM relatorio WHERE materia = ?", (materia,))
    resultado = cursor.fetchone() 

    if not resultado:

         
                dados = (materia, questoes, questoesCertas, horas, porcentagem)
                sql = "INSERT INTO relatorio (materia, questoes, questoesCertas, horas, porcentagem) VALUES (?, ?, ?, ?, ?)"
                cursor.execute(sql, dados)
                conn.commit()
        
    else:
         
        questoes_antigas = resultado[0]
        certas_antigas = resultado[1]
        hora_sql = resultado[2]


        

        questoes_novas = questoes + questoes_antigas
        certas_novas = questoesCertas + certas_antigas

        horas_totais = horas + hora_sql

        conta_porcentagem = (certas_novas/questoes_novas) * 100
        nova_porcentagem = round(conta_porcentagem)

        dados_atualizados = (questoes_novas, certas_novas, horas_totais, nova_porcentagem, materia)
        sql_2 = ("UPDATE relatorio SET questoes = ?, questoesCertas = ?, horas = ?, porcentagem =? WHERE materia = ?")
        cursor.execute(sql_2, dados_atualizados)
        conn.commit()



     
                

   
def mostrar_relatorio(conn):
    

    cursor = conn.cursor()

    cursor.execute("SELECT * FROM relatorio")
    dados = cursor.fetchall() #captura os dados
    
    return dados # retorna os dados


    

if __name__ =='__main__':


    #Abre a conexão
    conn = conectar()

    #Chama a função passando a conexão
    criar_tabela(conn)

    
    mostrar_relatorio(conn)


    conn.close()

