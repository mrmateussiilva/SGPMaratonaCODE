from flask import Flask, render_template, redirect, url_for,Blueprint
from flask_bootstrap import Bootstrap5
from form import LoginForm

from flask_wtf import CSRFProtect


# Blueprints
from pedidos import pedidos

app = Flask(__name__)
app.secret_key = 'mateus_top'
app.register_blueprint(pedidos.bp_pedidos)

bootstrap = Bootstrap5(app)
# app.config['BOOTSTRAP_BOOTSWATCH_THEME'] = 'materia'
csrf = CSRFProtect(app)


names = ["Mateus jose","Breno Polezi","mateus"]

@app.route("/home")
def home():
    return render_template("login/home.html")


@app.route("/",methods=["GET","POST"])
def index():
    form = LoginForm()
    message = ''
    if form.validate_on_submit():
        if form.name.data in names:
            return redirect(url_for('home'))
        else:
            message= "Informações incorretas tente novamente"
            return render_template("login/index.html",form=form,message=message)
        
    return render_template("login/index.html",form=form)


if __name__ == "__main__":
    app.run(debug=True)