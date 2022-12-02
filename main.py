from flask import Flask, render_template;


app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template("welcome.html", title="Network Manager")

@app.route("/login")
def login():
    return render_template("login.html", title="Inicio de Sesion")

@app.route("/register")
def register():
    return render_template("register.html", title="Registrate")