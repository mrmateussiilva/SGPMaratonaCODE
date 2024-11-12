from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap5
from flask_wtf import CSRFProtect
from form import PainelForm,TipoDeProdutoForm,FichaPedido,TotemForm

app = Flask(__name__)
app.secret_key = b'mateus jose da silva'
bootstrap = Bootstrap5(app)
csrf = CSRFProtect(app)


@app.route("/")
@app.route("/home")
def home():
    return render_template("index.html")


data_pedidos = [
    {"id":'1','descricao':'Painel Redondo BATMAN','value':'90,00','date_envio':'03/11/2024',"forma_envio":'SEDEX'},
    {"id":'2','descricao':'Painel Redondo BATMAN','value':'90,00','date_envio':'03/11/2024',"forma_envio":'SEDEX'},
    {"id":'3','descricao':'Painel Redondo BATMAN','value':'90,00','date_envio':'03/11/2024',"forma_envio":'SEDEX'},
]

@app.route("/pedidos")
def pedidos():
    titles = tuple(map(lambda t: t.replace('_'," ").title(),data_pedidos[0].keys()))
    return render_template("pedidos/index.html",data=data_pedidos,titles=titles)


@app.route("/pedidos/criar",methods=["GET","POST"])
def pedidos_criar():
    form_top = FichaPedido(idd='1')
    form_produto = TipoDeProdutoForm()
    form_painel = PainelForm()
    form_totem = TotemForm()
    if request.method == "GET":
        # print(form_top.csrf_token)
        
        return render_template(
            "pedidos/criar.html",form_top=form_top,form_produto=form_produto
            ,form_painel=form_painel,form_totem=form_totem
            )
    
    if request.method == "POST":
        # return f"{request.form}"
        if form_top.validate_on_submit():
            return f"{form_top}"
        else:
            return f"{request.form}"







if __name__ == "__main__":
    app.run(debug=True)