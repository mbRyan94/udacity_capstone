import os
from flask import Flask, jsonify, request
from flask_heroku import Heroku
from models import setup_db, Person, Dog
from flask_cors import CORS
from dotenv import load_dotenv
import sys
load_dotenv()


def create_app(test_config=None):

    app = Flask(__name__)

    heroku = Heroku(app)
    setup_db(app)
    app.config["SQLALCHEMY_DATABASE_URI"]

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

    @app.route('/api/persons', methods=['POST'])
    def db_add_person():
        try:
            req_data = request.get_json()
            name = req_data['name']
            catchphrase = req_data['catchphrase']
            print(req_data)
            new_person = Person(
                name=name, catchphrase=catchphrase)
            Person.insert(new_person)
            persons = Person.query.all()
            res_names = []
            for person in persons:
                # print('person: ', person)
                res_names.append({
                    "name": person.name,
                    "catchphrase": person.catchphrase
                })
            # print(res)
            return jsonify({"new_person": res_names})
        except Exception:
            print(sys.exc_info())
            return jsonify({"new_person": "did not work"})

    @app.route('/api/dogs', methods=['POST'])
    def db_add_dog():
        try:
            req_data = request.get_json()
            name = req_data['name']
            catchphrase = req_data['catchphrase']
            print(req_data)
            new_dog = Dog(
                name=name, catchphrase=catchphrase)
            Dog.insert(new_dog)
            dogs = Dog.query.all()
            res_names = []
            for dog in dogs:
                # print('person: ', person)
                res_names.append({
                    "name": dog.name,
                    "catchphrase": dog.catchphrase
                })
            # print(res)
            return jsonify({"new_dog": res_names})
        except Exception:
            print(sys.exc_info())
            return jsonify({"new_dog": "did not work"})

    return app


app = create_app()

if __name__ == '__main__':
    app.run()
