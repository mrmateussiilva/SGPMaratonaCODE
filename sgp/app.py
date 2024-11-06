from flask import Flask, render_template, redirect, url_for,Blueprint
from flask_bootstrap import Bootstrap5
from form import LoginForm
from flask_wtf import CSRFProtect
from pedidos import pedidos
from dotenv import load_dotenv
from os import getenv

load_dotenv(".env")
app = Flask(__name__)
app.secret_key = 'mateus_top'
app.register_blueprint(pedidos.bp_pedidos)

bootstrap = Bootstrap5(app)
# app.config['BOOTSTRAP_BOOTSWATCH_THEME'] = 'materia'
csrf = CSRFProtect(app)



@app.route("/")
@app.route("/home")
def home():
    return render_template("index.html")



@app.route("/login",methods=["GET","POST"])
def login():
    form = LoginForm()
    message = ''
    if form.validate_on_submit():
        user,password = getenv("ADMIN"),getenv("PASSWORD")
        if form.name_user.data != user and form.password_user.data != password:
            return render_template("login/index.html",form=form,message="Login invalido",flag_error=True)
        else:
            return redirect(url_for('home'))
               
    return render_template("login/index.html",form=form,flag_error=False)



if __name__ == "__main__":
    app.run(debug=True)