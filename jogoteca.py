from flask import Flask, render_template

app = Flask(__name__)

@app.route('/inicio')
def ola():
    lista = ['Tetris', 'Super Mario', 'Pokemon Gold']

    return render_template('lista.html', titulo='Jogos', 
                                        jogos=lista) # Jinja2 é a resposável por colocar conteúdo dinâmico nas páginas html

app.run()