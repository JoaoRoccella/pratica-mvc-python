import mysql.connector
from mysql.connector import Error
from dotenv import load_dotenv
from os import getenv

class Database:
    def __init__(self):
        load_dotenv()
        self.host = getenv('DB_HOST')
        self.database = getenv('DB_NAME')
        self.user = getenv('DB_USER')
        self.password = getenv('DB_PSWD')

    def conectar(self):
        try:
            self.connection = mysql.connector.connect(
                host=self.host,
                database=self.database,
                user=self.user,
                password=self.password
            )
            self.cursor = self.connection.cursor()
            print('Conexão ao banco de dados realizada com sucesso!')
        except Error as e:
            print(f'Error de conexão: {e}')

    def desconectar(self):
        self.connection.close()
        self.cursor.close()
        print('Conexão ao banco de dados encerrada com sucesso!')

    def executar(self, sql, params=None):
        try:
            self.cursor.execute(sql, params)
            self.connection.commit()
            return self.cursor
        except Error as e:
            print(f'Error de execução: {e}')
            return None