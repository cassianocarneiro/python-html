from flask import Flask #flask é a biblioteca, Flask é a classe

app = Flask("microblog")

# Agora, "app" é um programa que fica rodando e escutando a internet à espera de requisições.
# Flask faz a conexão de uma url com o python


@app.route("/") # Lincando a função "index" (abaixo) com uma rota de internet, ou seja, uma url
def index():
    return "Hello world!"

app.run()
