from flask import Flask
from flask_restful import Api

from fizzbuzz_controller import FizzBuzzController

app = Flask(__name__)
api = Api(app)

api.add_resource(FizzBuzzController, '/fizzbuzz/test/<int:input_var>')

app.run(port=5000, debug=True)
