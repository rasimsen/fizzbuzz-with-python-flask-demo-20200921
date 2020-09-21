# RED-GREEN-BLUE

import unittest

from fizzbuzz_service import FizzBuzzService


class FizzBuzzServiceTest(unittest.TestCase):
    def test_fizz(self):
        self.assertEqual("Fizz", FizzBuzzService.fb_validator(3))
        self.assertEqual("Fizz", FizzBuzzService.fb_validator(33))
        self.assertEqual("Fizz", FizzBuzzService.fb_validator(399))

    def test_buzz(self):
        self.assertEqual("Buzz", FizzBuzzService.fb_validator(5))
        self.assertEqual("Buzz", FizzBuzzService.fb_validator(50))
        self.assertEqual("Buzz", FizzBuzzService.fb_validator(500))

    def test_fizzbuzz(self):
        self.assertEqual("FizzBuzz", FizzBuzzService.fb_validator(15))
        self.assertEqual("FizzBuzz", FizzBuzzService.fb_validator(30))
        self.assertEqual("FizzBuzz", FizzBuzzService.fb_validator(300))

    def test_other(self):
        self.assertEqual(2, FizzBuzzService.fb_validator(2))
        self.assertEqual(7, FizzBuzzService.fb_validator(7))
        self.assertEqual(11, FizzBuzzService.fb_validator(11))

if __name__ == '__main__':
    unittest.main()
