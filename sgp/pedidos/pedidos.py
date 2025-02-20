from flask import Blueprint,render_template,request,redirect,url_for,flash
from .form import PainelForm,TipoDeProdutoForm,FichaPedido,TotemForm
from model import inserDB,get_all_pedidosDB
bp_pedidos = Blueprint('pedidos',__name__)



@bp_pedidos.route("/pedidos")
def home():
    return render_template("pedidos/index.html",pedidos=get_all_pedidosDB())


@bp_pedidos.route("/pedidos/criar",methods=["GET","POST"])
def criar():
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
    
    if form_top.validate_on_submit():
        # print()
        # return redirect(url_for("pedidos.criar"))
        print(request.form)

        if inserDB(request.form):
            flash("Pedido Criado com sucesso","success")
            messages = []
            return redirect(url_for('pedidos.criar'))
        else:
            flash("Error ao criar pedido","danger")
            return redirect(url_for('pedidos.criar'))
        