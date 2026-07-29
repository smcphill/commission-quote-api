from flask import Flask, abort, jsonify, render_template, request
from werkzeug.exceptions import HTTPException
from pydantic import BaseModel, Field, ValidationError
from typing import Literal
import random
import uuid

app = Flask(__name__)

COMMISSION_RATE = 0.1  # Flat commission rate for all quotes
CHAOS_RATE = 0.8
VALID_API_KEYS = ["alice", "bob"]
CHAOTIC_API_KEY = "bob"


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
    ensure_valid_api_key()
    chaos_mode = request.headers["api-key"] == CHAOTIC_API_KEY
    if chaos_mode:
        enact_chaos()

    data = request.get_json()
    if not data:
        return jsonify({"error": "Missing request"}), 400

    try:
        quote_request = QuoteRequest(**data)
    except ValidationError as e:
        invalid_fields = [err["loc"][0] for err in e.errors()]
        return jsonify({"error": f"Invalid {', '.join(invalid_fields)}"}), 400

    generated_quote = generate_quote(quote_request)

    return jsonify(generated_quote), 200


@app.errorhandler(HTTPException)
def handle_http_exception(error):
    return jsonify({"error": error.description}), error.code


@app.errorhandler(Exception)
def handle_unexpected_error(error):
    return jsonify({"error": "An unexpected error occurred"}), 500


def ensure_valid_api_key():
    api_key_payload = request.headers.get("api-key", [])
    # Validate API key
    if api_key_payload not in VALID_API_KEYS:
        abort(401)


def enact_chaos():
    # Chaos mode logic
    random_value = random.random()
    if random_value < CHAOS_RATE:

        if random_value < 0.3:
            # Simulate a server error
            abort(500)

        # Otherwise, close the underlying socket to simulate a connection reset
        socket_obj = request.environ.get("wsgi.input").raw._sock
        socket_obj.shutdown(2)  # 2 = SHUT_RDWR (disables reads and writes)
        socket_obj.close()


def generate_quote(request: QuoteRequest) -> dict:
    # Quote generation logic
    return {
        "quoteId": uuid.uuid4().hex,
        "commissionRate": COMMISSION_RATE,
        "totalCommission": request.loanAmount * COMMISSION_RATE,
    }
