import os
from flask import Flask, jsonify
from models import setup_db
from flask_cors import CORS
from dotenv import load_dotenv
load_dotenv()


def create_app(test_config=None):

    app = Flask(__name__)
    # setup_db(app)
    CORS(app)

    @app.route('/')
    def get_greeting():
        excited = os.getenv('EXCITED')
        greeting = "Hello"
        if excited == 'true':
            greeting = greeting + "!!!!!"
        return greeting

    @app.route('/coolkids')
    def be_cool():
        return "Be cool, man, be coooool! You're almost a FSND grad!"

    @app.route('/api/test')
    def api_test():
        return jsonify({"msg": "API is working!"})

    return app


app = create_app()

if __name__ == '__main__':
    app.run()
