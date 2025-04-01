from flask import Flask, render_template, request, redirect, url_for
from model.tarefa import Tarefa

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        titulo = request.form['titulo']
        data_conclusao = request.form['data_conclusao']
        tarefa = Tarefa(titulo=titulo, data_conclusao=data_conclusao)
        tarefa.salvar_tarefa()
        return redirect(url_for('index'))

    tarefas = Tarefa.listar_tarefas()
    
    return render_template(
        'index.html', 
        tarefas=tarefas, 
        title='Minhas Tarefas'
    )

@app.route('/update/<int:idTarefa>', methods = ['GET', 'POST'])
def editar(idTarefa):
    if request.method == 'POST':
        titulo = request.form['titulo']
        data_conclusao = request.form['data_conclusao']
        tarefa = Tarefa(id = idTarefa, titulo = titulo, data_conclusao = data_conclusao)
        tarefa.atualizar_tarefa()
        return redirect(url_for('index'))

    tarefas_banco = Tarefa.listar_tarefas()
    tarefa_selecionada = Tarefa.buscar_tarefa(idTarefa)
    return render_template(
        'index.html',
        tarefa_selecionada = tarefa_selecionada,
        tarefas = tarefas_banco,
        title = 'Editando tarefa | Minhas tarefas'
    )

@app.route('/delete/<int:idTarefa>')
def delete(idTarefa):
    Tarefa.apagar_tarefa(idTarefa)
    return redirect(url_for('index'))

