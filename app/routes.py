from app import app
from flask impor render_template

@app.route("/") # Para tal url, executar a função abaixo
@app.route("/index") # Também para essa url, executar a função abaixo
def index():
    return render_template("index.html")
