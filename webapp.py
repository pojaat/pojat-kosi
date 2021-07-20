from flask import Flask, redirect, render_template

app = Flask(__name__, static_folder="/root/pojat-kosi")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/index.html")
def return_homepage():
    return redirect("/")

@app.route("/tony")
def tony():
    return render_template("tony.html")

@app.route("/alibi")
def alibi():
    return render_template("alibi.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
