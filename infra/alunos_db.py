import sqlite3

db_name = "alunos.db"
table_name = "aluno"

sql_create_table = f"CREATE TABLE IF NOT EXISTS {table_name} (id integer PRIMARY KEY, nome text NOT NULL, matricula int NOT NULL);"

def createTable(cursor, sql):
    cursor.execute(sql)

def popularDb(cursor, id, nome, matricula):
    sql = f"INSERT INTO {table_name} (id, nome, matricula) VALUES (?, ?, ?)"
    cursor.execute(sql, (id, nome, matricula))

def init():
    connection = sqlite3.connect(db_name)
    cursor = connection.cursor()
    createTable(cursor, sql_create_table)
    try:
        popularDb(cursor, 1, "Thomas Alexandre", 1000)
        popularDb(cursor, 2, "Lucio Mendes", 1001)
        popularDb(cursor, 3, "Vinicius Williams", 1002)
    except:
        pass
    cursor.close()
    connection.commit()
    connection.close()
    
init()