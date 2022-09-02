import mysql.connector
from mysql.connector import errorcode
try:
    db_conexão = mysql.connector.connect(host='localhost', user='root', password='', database='clientes')
    cursor = db_conexão.cursor()
    sql = 'CREATE TABLE IF NOT EXISTS pessoa(ID int not null auto_increment unique, Nome varchar(50), CPF varchar(15) unique, Telefone varchar(20), Conta_corrente varchar(15) unique, Agência varchar(10), Banco varchar(30),Cidade varchar(30), Sigla varchar (2), Nacionalidade varchar(20), Empresa int, Função varchar(20));'
    cursor.execute(sql)
    sql = 'INSERT INTO pessoa(Nome, CPF, Telefone, Conta_corrente, Agência, Banco, Cidade, Sigla, Nacionalidade, Empresa, Função) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
    values = (str(input('Digite seu nome: ')),str(input('Digite o seu CPF: ')),str(input('Digite seu telefone: ')),str(input('Digite o número da conta corrente: ')),str(input('Digite a agência: ')),str(input('Digite o banco: ')),str(input('Digite a cidade: ')),str(input('Digite a sigla do estado: ')),str(input('Digite sua nacionalidade: ')),str(input('Digite o ID da empresa: ')), str(input('Digite sua função na empresa: ')))
    cursor.execute(sql, values)
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
