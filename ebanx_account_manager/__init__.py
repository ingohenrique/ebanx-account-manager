from flask import Flask, request, jsonify
import logging
from services.account_service import AccountService
from data.account_handler import AccountHandler

accounts = {}

account_service = AccountService(AccountHandler())

def create_app():
    """
    Creates and configures the Flask app.
    """
    app = Flask(__name__)
    logging.info('App initialized.')
    
    @app.route('/')
    def health():
        return 'The app is running...'
    
    @app.route('/reset', methods=['POST'])
    def reset():
        accounts = {}
        return {
            'response':'The accounts have been reset',
            'status':200
        }

    @app.route('/balance', methods=['GET'])
    def balance():
        return {
            'response':'',
            'status':200
        }

    @app.route('/event', methods=['POST'])
    def event():
        data = request.get_json()
        if data['type'] == 'deposit':
            account = account_service.deposit(data['destination'], data['amount'])
            return jsonify({'destination':{'id':f'{account.account_id}', 'amount':f'{account.balance}'}})
       
    
    return app
    
