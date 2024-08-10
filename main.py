from ebanx_account_manager import create_app
import os

# Creates the Flask application
app = create_app()

if __name__ == '__main__':
    host = os.environ.get('FLASK_RUN_HOST', '0.0.0.0')
    port = int(os.environ.get('FLASK_RUN_PORT', 8000))

    app.run(host=host, port=port)
