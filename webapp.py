from flask import Flask, redirect, render_template

app = Flask(__name__, static_folder="/root/pojat-kosi")

@app.route("/")
def index():
    return render_template("index.html")

@app.route(f'/<file>')
def hello_world(file):
    return render_template(file)

@app.route("/alibi.html")
def alibi():
    datal = list()
    with open("alibi.txt", "r") as file:
        for i in file.readlines():
            datal.append(i)
            print(i)

    return render_template("/alibi.html",data=datal)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
