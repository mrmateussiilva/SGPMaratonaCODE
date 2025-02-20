from flask_wtf import FlaskForm
from wtforms import DecimalField,StringField,DateField,SubmitField,SelectField,IntegerField,FileField,BooleanField,RadioField
from wtforms.validators import ReadOnly,DataRequired
import wtforms


choices_envio = [
    ("sedex","SEDEX"),
    ("pac","PAC"),
    ("retirada","RETIRADA"),
    ("entrega_colatina","ENTREGA COLATINA"),
    ("motoboy vix","MOTOBOY VIX"),
    ("a_combinar","A COMBINAR"),
]

choices_client = [
    # id_client, name_client
    ("0","Mateus Jośe da Silva"),
    ("1","Breno Polezi"),
    ("2","Robson Cantarela"),
]

choices_produtos = [
    (' ',' '),
    ('painel','Painel'),
    ('totem','Totem'),
    ('adesivo','Adesivo'),
]

class FichaPedido(FlaskForm):
    idd = IntegerField("Número do Pedido",validators=[ReadOnly()])
    name_client = SelectField("Nome do cliente",choices=choices_client, validators=[DataRequired()])
    data_entrada = DateField(label="Data de Entrada", validators=[DataRequired()])
    data_envio = DateField(label="Data de envio", validators=[DataRequired()])
    forma_de_envio = SelectField("Selecione a forma de envio",choices=choices_envio, validators=[DataRequired()])
    observacao = StringField("")
    btn_save = SubmitField("Salvar",)



class TipoDeProdutoForm(FlaskForm):
    opcoes = SelectField("Selecione o tipo de produto",default=' ',choices=choices_produtos)



choices_tecido = [
    ("tactel","Tactel"),
    ("malha","Malha"),
    ("oxfordini","Oxfordini"),
    ("oxford","Oxford"),
    ("oxford","Oxford"),
]
choices_toten = [
    ("mdf_3mm","3mm"),
    ("mdf_6mm","6mm"),
    ("pvc","PVC"),
]

class PainelForm(FlaskForm):
    descricao = StringField("Descrição do Painel")
    tamanho = StringField("Tamanho do Painel")
    imagem_ficha = FileField()
    value = DecimalField("Valor do Painel")
    observacao = StringField("Observação")

    # Costura
    tipo_tecido = SelectField(label="Tipo de tecido",choices=choices_tecido)
    overloque = BooleanField("Overloque ?")
    elastico = BooleanField("Elastico ?")
    bainha = BooleanField("Bainha ?")
    
    # Salvar
    adicionar = SubmitField("Adicionar")
    
    
    
class TotemForm(FlaskForm):
    descricao = StringField("Descrição do Totem")
    tamanho = StringField("Tamanho do Totem")
    imagem_ficha = FileField()
    value = DecimalField("Valor do Totem")
    observacao = StringField("Observção")

    # Costura
    espessura_totem = SelectField(label="Material",choices=choices_toten)
    com_p_or_sem = RadioField("Com pé ?",choices=[
        ('sim',"Sim"),
        ('nao',"Não"),
    ])
    
    # Salvar
    adicionar = SubmitField("Adicionar")
    
