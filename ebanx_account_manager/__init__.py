from flask import Flask
import logging

accounts = {}

def create_app():
    """
    Creates and configures the Flask app.
    """
    app = Flask(__name__)
    logging.info("App initialized.")
    
    @app.route("/")
    def health():
        return "The app is running..."
    
    @app.route("/reset", methods=["POST"])
    def reset():
        accounts = {}
        return {
            "response":"The accounts have been reset",
            "status":200
        }

    @app.route("/balance", methods=["GET"])
    def balance():
        return {
            "response":"",
            "status":200
        }

    @app.route("/event", methods=["POST"])
    def event():
        return {
            "response":"",
            "status":200
        }
    
    return app
    
