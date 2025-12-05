from flask import Flask, jsonify, render_template
import json

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/data")
def data():
    with open("data.json", "r", encoding="UTF-8") as f:
        return jsonify(json.loads(f.read()))


app.run(host="0.0.0.0", debug=True, port=5000)
