from flask import Flask, redirect, render_template

app = Flask(__name__, static_folder="/root/pojat-kosi")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/index.html")
def return_homepage():
    return redirect("/")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
