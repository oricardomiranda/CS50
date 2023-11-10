# Uses a single route

from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST": #Post hides the URL names
        return render_template("greet.html", name=request.form.get("name", "world"))
    return render_template("index.html")
