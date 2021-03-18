from app import app
from flask import render_template

@app.route("/") # Para tal url, executar a função abaixo
@app.route("/index") # Também para essa url, executar a função abaixo
def index():
    user = {'username': 'Mr. Cassiano'}
    posts = [
        {'author': {'username' : 'Maria'}, 'body': "Lancei o míssel."},
        {'author': {'username' : 'Alexei'}, 'body': "Tá bom, Maria."}
    ]
    return render_template("index.html", user=user, posts=posts)
