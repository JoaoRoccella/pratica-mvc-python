from flask import Flask, render_template, request, redirect, url_for
from model.tarefa import Tarefa

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        titulo = request.form['titulo']
        data_conclusao = request.form['data_conclusao']
        tarefa = Tarefa(titulo=titulo, data_conclusao=data_conclusao)
        tarefa.salvar_tarefa()
        return redirect(url_for('index'))
    
    tarefas = Tarefa().listar_tarefas()
    return render_template('index.html', tarefas=tarefas)

@app.route("/delete/<int:id>")
def delete(id):
    tarefa = Tarefa(id=id)
    tarefa.apagar_tarefa()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)