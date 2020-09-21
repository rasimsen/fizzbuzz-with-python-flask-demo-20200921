class FizzBuzzService:
    def fb_validator(input_var):
        if input_var % 15 == 0:
            return "FizzBuzz"
        elif input_var % 3 == 0:
            return "Fizz"
        elif input_var % 5 == 0:
            return "Buzz"
        else:
            return input_var
