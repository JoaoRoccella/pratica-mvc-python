from model.database import Database
from datetime import datetime

class Tarefa:
    def __init__(self, titulo, id=None, data_conclusao=None):
        self.id = id
        self.titulo = titulo
        self.data_conclusao = data_conclusao

    def salvar_tarefa(self):
        """Salva uma nova tarefa no banco de dados."""
        db = Database()
        db.conectar()

        sql = 'INSERT INTO tarefa (titulo, data_conclusao) VALUES (%s, %s);'
        params = (self.titulo, self.data_conclusao)
        db.executar(sql, params)
        db.desconectar()

    @staticmethod
    def listar_tarefas():
        """Retorna uma lista com todas as tarefas cadastradas."""
        db = Database()
        db.conectar()

        sql = 'SELECT id, titulo, data_conclusao FROM tarefa;'
        tarefas = db.consultar(sql)
        db.desconectar()
        return tarefas if tarefas else []

    @staticmethod
    def apagar_tarefa(id_tarefa):
        """Apaga uma tarefa cadastrada no banco de dados."""
        db = Database()
        db.conectar()

        sql = 'DELETE FROM tarefa WHERE id = %s'
        params = (id_tarefa,) # Precisa passar como tupla? (a, b, c, ...) SIM!
        db.executar(sql, params)
        db.desconectar()
    
    def atualizar_tarefa(self):
        """Altera as informações de uma tarefa."""
        db = Database()
        db.conectar()

        sql = 'UPDATE tarefa SET titulo = %s, data_conclusao = %s where id = %s;'
        params = (self.titulo, self.data_conclusao, self.id)
        db.executar(sql, params)
        db.desconectar()

    def carregar_tarefa(idTarefa):
        """Carrega uma tarefa do específica do banco de dados na memória."""
        db = Database()
        db.conectar()

        sql = 'SELECT id, titulo, data_conclusao FROM tarefa where id = %s;'
        params = (idTarefa,)
        resultado = db.consultar(sql, params)
        db.desconectar()

        if resultado:
            tarefa_selecionada = resultado[0]  # Pegamos o primeiro (e único) dicionário retornado

            # Verifica se a data_conclusao é um objeto datetime e formata corretamente
            data_formatada = (
                tarefa_selecionada["data_conclusao"].strftime('%Y-%m-%d') 
                if isinstance(tarefa_selecionada["data_conclusao"], datetime) 
                else tarefa_selecionada["data_conclusao"]
            )

            return Tarefa(
                id=tarefa_selecionada["id"],
                titulo=tarefa_selecionada["titulo"],
                data_conclusao=data_formatada
            )
        
        return None
    
    
