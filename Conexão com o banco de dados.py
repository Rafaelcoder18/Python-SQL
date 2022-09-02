import mysql.connector
from mysql.connector import errorcode
try:
    db_conexão = mysql.connector.connect(host='localhost', user='root', password='', database='clientes')
    cursor = db_conexão.cursor()
    cursor.close()
    db_conexão.commit()
    db_conexão.close()
except mysql.connector.Error as error:
    if error.errno == errorcode.ER_BAD_DB_ERROR:
        print('O banco de dados não existe!!')
    elif error.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print('Usuáro ou senha inválidos!!')
    else:
        print(error)
else:
    db_conexão.close()