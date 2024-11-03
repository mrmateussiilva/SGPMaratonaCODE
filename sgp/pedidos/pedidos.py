from flask import Blueprint,render_template
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


@bp_pedidos.route("/pedidos/criar")
def pedidos_criar():
    form_top = FichaPedido(idd='1')
    form_produto = TipoDeProdutoForm()
    form_painel = PainelForm()
    form_totem = TotemForm()
    return render_template(
        "pedidos/criar.html",form_top=form_top,form_produto=form_produto
        ,form_painel=form_painel,form_totem=form_totem
        )
    
    # return render_template("pedidos/criar.html",form_top=form_top,form=produto,sub_form=sub_form)
    
