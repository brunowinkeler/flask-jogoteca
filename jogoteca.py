from flask import Flask, render_template

app = Flask(__name__)

@app.route('/inicio')
def ola():
    return render_template('lista.html', titulo='Jogos') # Jinja2 é a resposável por colocar conteúdo dinâmico nas páginas html

app.run()