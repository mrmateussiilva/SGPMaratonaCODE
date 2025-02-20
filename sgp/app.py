from flask import Flask, render_template, request,flash,redirect,url_for
from flask_bootstrap import Bootstrap5
from flask_wtf import CSRFProtect


# Blueprints
from pedidos.pedidos import bp_pedidos

app = Flask(__name__)
app.register_blueprint(bp_pedidos)
app.secret_key = b'mateus jose da silva'
bootstrap = Bootstrap5(app)
csrf = CSRFProtect(app)

data = {
        "idd": "5",
        "name_client": "Teste do mobile ",
        "data_entrada": "2025-02-20",
        "data_envio": "2025-02-28",
        "forma_de_envio": "entrega_colatina",
            "observacao": "",
}





@app.route("/")
@app.route("/home")
def home():    
    return render_template("index.html",pedido=data)



if __name__ == "__main__":
    app.run(debug=True)