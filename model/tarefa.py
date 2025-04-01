from datetime import datetime
from model.database import Database

class Tarefa:
    def __init__(self, titulo, id=None, data_conclusao=None):
        self.id = id
        self.titulo = titulo
        self.data_conclusao = data_conclusao

    def salvar_tarefa(self):
        """Salva uma nova tarefa no banco de dados."""
        db = Database()
        db.conectar()

        sql = 'INSERT INTO tarefa (titulo, data_conclusao) VALUES (%s, %s)'
        params = (self.titulo, self.data_conclusao)
        db.executar(sql, params)
        db.desconectar()

    @staticmethod
    def listar_tarefas():
        """Retornar uma lista com todas as tarefas cadastradas."""
        db = Database()
        db.conectar()

        sql = 'SELECT id, titulo, data_conclusao FROM tarefa'
        tarefas = db.consultar(sql)
        db.desconectar()
        return tarefas if tarefas else []
    
    @staticmethod
    def buscar_tarefa(idTarefa):
        """Busca uam tarefa específica do banco de dados e carrega na memória."""
        db = Database()
        db.conectar()

        sql = 'SELECT id, titulo, data_conclusao FROM tarefa WHERE id = %s'
        params = (idTarefa,)
        resultado = db.consultar(sql, params)
        db.desconectar()

        if resultado:
            tarefa_selecionada = resultado[0]

            data_formatada = (
                tarefa_selecionada['data_conclusao'].strftime('%Y-%m-%d')
                if isinstance(tarefa_selecionada['data_conclusao'], datetime)
                else tarefa_selecionada['data_conclusao']
            )

            return Tarefa(
                id = tarefa_selecionada['id'],
                titulo = tarefa_selecionada['titulo'],
                data_conclusao = data_formatada
            )
        
        return None
    
    def atualizar_tarefa(self):
        """Altera as informações de uma tarefa."""
        db = Database()
        db.conectar()

        sql = 'UPDATE tarefa SET titulo = %s, data_conclusao = %s WHERE id = %s'
        params = (self.titulo, self.data_conclusao, self.id)
        db.executar(sql, params)
        db.desconectar()

    @staticmethod
    def apagar_tarefa(idTarefa):
        """Apaga uma tarefa cadastrada no banco de dados."""
        db = Database()
        db.conectar()

        sql = 'DELETE FROM tarefa WHERE id = %s'
        params = (idTarefa,) # Precisa passar como tupla? (a, b, c, ...) SIM!
        db.executar(sql, params)
        db.desconectar()
    
