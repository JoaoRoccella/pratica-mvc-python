from model.database import Database

class Tarefa:
    def __init__(self, id=None, titulo=None, data_conclusao=None):
        self.id = id
        self.titulo = titulo
        self.data_conclusao = data_conclusao

    def salvar_tarefa(self):
        """Salva uma nova tarefa no banco de dados."""
        db = Database()
        db.conectar()
        
        if db.connection is None and db.cursor is None:
            return None
        
        sql = 'INSERT INTO tarefas (titulo, data_conclusao) VALUES (%s, %s)'
        params = (self.titulo, self.data_conclusao)
        db.executar(sql, params)
        db.desconectar()

    @staticmethod
    def listar_tarefas():
        """Retorna uma lista com todas as tarefas cadastradas no banco de dados."""
        db = Database()
        db.conectar()
        
        if db.connection is None and db.cursor is None:
            return None
        
        sql = 'SELECT id, titulo, data_conclusao FROM tarefas'
        tarefas = db.consultar(sql)
        db.desconectar()
        return tarefas if tarefas else []
    
    def apagar_tarefa(self):
        """Apaga uma tarefa do banco de dados."""
        db = Database()
        db.conectar()

        if db.connection is None and db.cursor is None:
            return None
        
        sql = 'DELETE FROM tarefas WHERE id = %s'
        params = (self.id,)
        db.executar(sql, params)
        db.desconectar()

