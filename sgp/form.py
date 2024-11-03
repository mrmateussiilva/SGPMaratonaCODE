from flask_wtf import FlaskForm, CSRFProtect
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length




class LoginForm(FlaskForm):
    name = StringField("Insira o seu nome",validators=[DataRequired(),Length(10,100)])
    submit = SubmitField("Enviar")
