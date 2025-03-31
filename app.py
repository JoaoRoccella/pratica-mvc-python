from flask import Flask, render_template, request, redirect, url_for
from model.tarefa import Tarefa

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        titulo = request.form['titulo']
        data_conclusao = request.form['data_conclusao']
        tarefa = Tarefa(titulo=titulo, data_conclusao=data_conclusao)
        tarefa.salvarTarefa()
        return redirect(url_for('index'))

    tarefas = Tarefa.listarTarefas()
    return render_template('index.html', tarefas=tarefas, title='Minhas Tarefas')

@app.route('/delete/<int:idTarefa>')
def delete(idTarefa):
    Tarefa.apagarTarefa(idTarefa)
    return redirect(url_for('index'))

# Desenvolva uma nova funcionalidade para a nossa agenda: editar uma tarefa no próprio formulário da página de cadastro de tarefas.
# -> A aplicação deve permitir a edição de uma tarefa que foi selecionada da lista de tarefas
# -> Lembre-se de criar um método na classe Tarefa, uma rota no app.py e o código de front-end necessário para executar a ação de edição da tarefa
# -> Pesquise a respeito dos métodos HTTP que podem ser usados para essa finalidade e adapte uma solução em Python
