import os
from flask import Flask, jsonify, request
from flask_heroku import Heroku
from models import setup_db, Person
from flask_cors import CORS
from dotenv import load_dotenv
import sys
load_dotenv()


def create_app(test_config=None):

    app = Flask(__name__)
    heroku = Heroku(app)
    setup_db(app)
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

    @app.route('/api/db', methods=['POST'])
    def db_test():
        try:
            data = request.get_json()

            print(data)
            new_person = Person(
                name="Pipsii", catchphrase="This is the catchphrase")
            Person.insert(new_person)
            persons = Person.query.all()
            print(persons)
            return jsonify({"new_person": "works"})
        except Exception:
            print(sys.exc_info())
            return jsonify({"new_person": "did not work"})

    return app


app = create_app()

if __name__ == '__main__':
    app.run()
