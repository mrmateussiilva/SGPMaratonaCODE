from flask import Flask, render_template, request,flash,redirect,url_for
from flask_bootstrap import Bootstrap5
from flask_wtf import CSRFProtect
from form import PainelForm,TipoDeProdutoForm,FichaPedido,TotemForm
from model import inserDB,get_all_pedidosDB


app = Flask(__name__)
app.secret_key = b'mateus jose da silva'
bootstrap = Bootstrap5(app)
csrf = CSRFProtect(app)

@app.route("/")
@app.route("/home")
def home():    
    return render_template("index.html",pedidos=get_all_pedidosDB())


@app.route("/pedidos/criar",methods=["GET","POST"])
def pedidos_criar():
    idd = len(get_all_pedidosDB())
    form_top = FichaPedido(idd=idd)
    form_produto = TipoDeProdutoForm()
    form_painel = PainelForm()
    form_totem = TotemForm()
    if request.method == "GET":        
        return render_template(
            "pedidos/criar.html",form_top=form_top,form_produto=form_produto
            ,form_painel=form_painel,form_totem=form_totem
            )
    
    if request.method == "POST":
        if inserDB(request.form):
            flash("Pedido Criado com sucesso","info")
            return redirect('/home')
        else:
            flash("Error ao criar pedido","error")
            return redirect('/home')
        
if __name__ == "__main__":
    app.run(debug=True)