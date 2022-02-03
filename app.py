from flask import Flask, redirect, render_template, request


app = Flask(__name__)


@app.route("/")
def hello_world():
    return redirect("/home")


@app.route("/home")
def home():
    name = request.args.get("name")
    if name == "name":
        return render_template("home.html", name="pavouk")
    else:
        return render_template("home.html", name=name)

