from dotenv import dotenv_values
from flask import Flask, abort, jsonify, render_template, request
from werkzeug.exceptions import HTTPException
from pydantic import BaseModel, Field, ValidationError
from typing import Literal
import random
import uuid

app = Flask(__name__)

# TODO extract config into its own concern (app.config)
config = dotenv_values(".env")
COMMISSION_RATE: float = float(config.get("COMMISSION_RATE", 0))
CHAOS_RATE: float = float(config.get("CHAOS_RATE", 0))
CHAOS_MODE_HEADER: str = config.get("CHAOS_MODE_HEADER", "")
CHAOS_MODE: bool = config.get("CHAOS_MODE", "false").lower() == "true"

# TODO DRY up sourcing lists from config
VALID_API_KEYS: list = [
    value.strip()
    for value in config.get("VALID_API_KEYS", "").split(",")
    if value.strip()
]
DISALLOWED_API_KEYS: list = [
    value.strip()
    for value in config.get("DISALLOWED_API_KEYS", "").split(",")
    if value.strip()
]
RISK_BANDS: list = [
    value.strip() for value in config.get("RISK_BANDS", "").split(",") if value.strip()
]


class QuoteRequest(BaseModel):
    # Quote request schema
    loanAmount: int = Field(..., ge=1000, le=5000000)
    loanTermInMonths: int = Field(..., ge=1, le=240)
    riskBand: Literal[tuple(RISK_BANDS)]


@app.route("/")
def index():
    return render_template("index.html", risk_bands=RISK_BANDS)


@app.route("/api/quote", methods=["POST"])
def request_quote():
    ensure_valid_api_key()
    enact_chaos(requested=request.headers.get(CHAOS_MODE_HEADER) == "true")

    data = request.get_json()
    if not data:
        return jsonify({"error": "Missing request"}), 400

    try:
        quote_request = QuoteRequest(**data)
    except ValidationError as e:
        # TODO this implememtation is fairly magical. Revisit Pydantic Validators, and implement a more robust error presenter
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
    # Validate API key
    # TODO: make this Flask middleware.
    api_key_payload = request.headers.get("api-key", [])
    if api_key_payload not in VALID_API_KEYS or api_key_payload in DISALLOWED_API_KEYS:
        abort(401)


def enact_chaos(requested: bool):
    # as per CHAOS MODE and `requested`, simulate a server or connection reset error
    # TODO: extract this into a separate concern (e.g. app.chaos)
    random_value = random.random()
    if CHAOS_MODE or (requested and random_value < CHAOS_RATE):

        # 50% of the time, simulate a server error
        if random_value < CHAOS_RATE / 2:
            abort(500)

        # 50% of the time, simulate a connection reset (close the underlying socket)
        socket_obj = request.environ.get("wsgi.input").raw._sock
        socket_obj.shutdown(2)  # 2 = SHUT_RDWR (disables reads and writes)
        socket_obj.close()


def generate_quote(request: QuoteRequest) -> dict:
    # Quote generation logic. `QuoteRequest.riskBand`` is not used in the calculation.
    # TODO: this should be extracted into a separate concern (e.g. app.quote_generator)
    return {
        "quoteId": uuid.uuid4().hex,
        "commissionRate": COMMISSION_RATE,
        "totalCommission": request.loanAmount * COMMISSION_RATE,
    }
