from flask import Flask, jsonify, render_template, request
from werkzeug.exceptions import HTTPException
from pydantic import BaseModel, Field, ValidationError
from typing import Literal

app = Flask(__name__)


class QuoteRequest(BaseModel):
    # Quote request schema
    loanAmount: int = Field(..., ge=1000, le=5000000)
    loanTermInMonths: int = Field(..., ge=1, le=240)
    riskBand: Literal["BELOW_AVERAGE", "AVERAGE", "VERY_GOOD", "EXCELLENT"]


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/api/quote", methods=["POST"])
def request_quote():
    data = request.get_json()
    if not data:
        return jsonify({"error": "Missing request"}), 400

    try:
        QuoteRequest(**data)
    except ValidationError as e:
        invalid_fields = [err["loc"][0] for err in e.errors()]
        return jsonify({"error": f"Invalid {', '.join(invalid_fields)}"}), 400

    return jsonify({"quoteId": "123", "commissionRate": 0.1, "totalCommission": 100000})

@app.errorhandler(HTTPException)
def handle_http_exception(error):
    return jsonify({"error": error.description}), error.code


@app.errorhandler(Exception)
def handle_unexpected_error(error):
    return jsonify({"error": "An unexpected error occurred"}), 500