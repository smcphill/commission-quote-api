from flask import Flask, jsonify, render_template

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/api/quote", methods=["POST"])
def request_quote():
    return jsonify({"quoteId": "123", "commissionRate": 0.1, "totalCommission": 100000})
