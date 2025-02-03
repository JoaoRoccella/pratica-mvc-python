from model.database import Database

class Tarefa:
    def __init__(self, id=None, titulo=None, data_conclusao=None):
        self.id = id
        self.titulo = titulo
        self.data_conclusao = data_conclusao

    def salvar_tarefa(self):
        db = Database()
        db.conectar()
        sql = 'INSERT INTO tarefas (titulo, data_conclusao) VALUES (%s, %s)'
        params = (self.titulo, self.data_conclusao)
        db.executar(sql, params)
        db.desconectar()

    def listar_tarefas(self):
        db = Database()
        db.conectar()
        sql = 'SELECT * FROM tarefas'
        db.executar(sql)
        tarefas = db.cursor.fetchall()
        db.desconectar()
        return tarefas
    
    def apagar_tarefa(self):
        db = Database()
        db.conectar()
        sql = 'DELETE FROM tarefas WHERE id = %s'
        params = (self.id,)
        db.executar(sql, params)
        db.desconectar()

