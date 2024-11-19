from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route("/", methods=["POST", "GET"])
def index():
    atbilde = requests.get("https://api.chucknorris.io/jokes/random")
    joks = atbilde.json()
    joks1 = atbilde.text
    print(type(joks))
    print("----")
    print(type(joks1))
    return render_template("index.html", joks = joks["value"])

if __name__ == "main":
    app.run(port = 5000)