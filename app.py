from flask import Flask, redirect, render_template, url_for

app = Flask(__name__)

@app.route(rule="/")
def hello():
    return render_template("index.html")

if __name__=="__main__":
    app.run(debug=True)