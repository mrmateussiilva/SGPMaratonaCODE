from flask_wtf import FlaskForm, CSRFProtect
from wtforms import StringField, SubmitField,PasswordField
from wtforms.validators import DataRequired, Length




class LoginForm(FlaskForm):
    name_user = StringField("Insira o seu nome",validators=[DataRequired()])
    password_user = PasswordField("Insira a sua Senha:",validators=[DataRequired()])
    submit = SubmitField("Entrar")
