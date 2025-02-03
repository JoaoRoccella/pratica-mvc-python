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
        self.connection = None
        self.cursor = None

    def conectar(self):
        """Estabelece a conexão com o banco de dados."""
        try:
            self.connection = mysql.connector.connect(
                host=self.host,
                database=self.database,
                user=self.user,
                password=self.password
            )
            if self.connection.is_connected():
                self.cursor = self.connection.cursor(dictionary=True)
                print('Conexão ao banco de dados realizada com sucesso!')
        except Error as e:
            print(f'Error de conexão: {e}')
            self.connection = None
            self.cursor = None

    def desconectar(self):
        """Encerra a conexão com o banco de dados e o cursor, se existirem."""
        if self.cursor:
            self.cursor.close()
        if self.connection:
            self.connection.close()
            print('Conexão ao banco de dados encerrada com sucesso!')

    def executar(self, sql, params=None):
        """Executa uma instrução SQL no banco de dados."""
        if self.connection is None and self.cursor is None:
            print('Conexão ao banco de dados não estabelecida!')
            return None
        
        try:
            self.cursor.execute(sql, params)
            self.connection.commit()
            return self.cursor
        except Error as e:
            print(f'Error de execução: {e}')
            return None
        
    def consultar(self, sql, params=None):
        """Executa uma consulta SQL no banco de dados."""
        if self.connection is None and self.cursor is None:
            print('Conexão ao banco de dados não estabelecida!')
            return None
        
        try:
            self.cursor.execute(sql, params)
            return self.cursor.fetchall()
        except Error as e:
            print(f'Error de consulta: {e}')
            return None