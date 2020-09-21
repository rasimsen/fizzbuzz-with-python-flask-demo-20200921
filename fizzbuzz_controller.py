from flask_restful import Resource

from fizzbuzz_service import FizzBuzzService


# GET, PUT, POST, DELETE, OPTION etc..

class FizzBuzzController(Resource):
    def get(self, input_var):
        return FizzBuzzService.fb_validator(input_var)
