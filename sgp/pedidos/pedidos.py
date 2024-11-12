from flask import Blueprint,render_template,request,redirect,url_for
from .form import PainelForm,TipoDeProdutoForm,FichaPedido,TotemForm
bp_pedidos = Blueprint('pedidos',__name__)


data_pedidos = [
    {"id":'1','descricao':'Painel Redondo BATMAN','value':'90,00','date_envio':'03/11/2024',"forma_envio":'SEDEX'},
    {"id":'2','descricao':'Painel Redondo BATMAN','value':'90,00','date_envio':'03/11/2024',"forma_envio":'SEDEX'},
    {"id":'3','descricao':'Painel Redondo BATMAN','value':'90,00','date_envio':'03/11/2024',"forma_envio":'SEDEX'},
]

@bp_pedidos.route("/pedidos")
def pedidos():
    titles = tuple(map(lambda t: t.replace('_'," ").title(),data_pedidos[0].keys()))
    return render_template("pedidos/index.html",data=data_pedidos,titles=titles)


@bp_pedidos.route("/pedidos/criar",methods=["GET","POST"])
def pedidos_criar():
    form_top = FichaPedido(idd='1')
    form_produto = TipoDeProdutoForm()
    form_painel = PainelForm()
    form_totem = TotemForm()
    if request.method == "GET":
        print(form_top.idd.data)
        
        return render_template(
            "pedidos/criar.html",form_top=form_top,form_produto=form_produto
            ,form_painel=form_painel,form_totem=form_totem,form=form_top
            )
    
    if request.method == "POST":
        print(form_top.idd.data)
            
