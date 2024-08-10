from flask import Flask, request, jsonify, make_response
from services.account_service import AccountService
from data.account_handler import AccountHandler

account_service = AccountService(AccountHandler())


def create_app():
    """
    Creates and configures the Flask app.
    """
    app = Flask(__name__)

    @app.route("/reset", methods=["POST"])
    def reset():
        account_service.reset()
        response = make_response("OK", 200)
        response.mimetype = "text/plain"
        return response

    @app.route("/balance", methods=["GET"])
    def balance():
        account_id = request.args.get("account_id")
        account = account_service.get(account_id)
        if account:
            return jsonify(account.balance), 200
        else:
            return jsonify(0), 404

    @app.route("/event", methods=["POST"])
    def event():
        data = request.get_json()
        if data["type"] == "deposit":
            account = account_service.deposit(
                data["destination"], data["amount"]
            )
            return (
                jsonify(
                    {
                        "destination": {
                            "id": account.account_id,
                            "balance": account.balance,
                        }
                    }
                ),
                201,
            )
        if data["type"] == "withdraw":
            account = account_service.withdraw(
                data["origin"], data["amount"]
            )
            if account:
                return (
                    jsonify(
                        {
                            "origin": {
                                "id": account.account_id,
                                "balance": account.balance,
                            }
                        }
                    ),
                    201,
                )
            else:
                return jsonify(0), 404

        if data["type"] == "transfer":
            origin, destination = account_service.transfer(
                data["origin"], data["amount"], data["destination"]
            )
            if origin and destination:
                return (
                    jsonify(
                        {
                            "origin": {
                                "id": origin.account_id,
                                "balance": origin.balance,
                            },
                            "destination": {
                                "id": destination.account_id,
                                "balance": destination.balance,
                            },
                        }
                    ),
                    201,
                )
            else:
                return jsonify(0), 404

    return app
