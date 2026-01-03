'''
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/greet")
def greet():
    return render_template("greet.html", name=request.args.get("name", "world"))


'''

from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/greet", methods=["GET", "POST"])
def greet():
    if request.method == "POST":
        return render_template("greet.html", name=request.form.get("name", "world"))
    return render_template('index.html')



if __name__ == "__main__":
    app.run()
    