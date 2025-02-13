from flask import Flask, render_template, request,flash,redirect,url_for
from flask_bootstrap import Bootstrap5
from flask_wtf import CSRFProtect
from form import PainelForm,TipoDeProdutoForm,FichaPedido,TotemForm
from model import get_all_pedidosDB

# Blueprints
from pedidos.pedidos import bp_pedidos

app = Flask(__name__)
app.register_blueprint(bp_pedidos)
app.secret_key = b'mateus jose da silva'
bootstrap = Bootstrap5(app)
csrf = CSRFProtect(app)

@app.route("/")
@app.route("/home")
def home():    
    return render_template("index.html",pedidos=get_all_pedidosDB())



if __name__ == "__main__":
    app.run(debug=True)