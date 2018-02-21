from unittest import TestCase
from homeworks.task7.app.low_sqrt import find_the_lower_square, start_function

__author__ = 'nshumakov'


class TestLowerSquare(TestCase):
    def setUp(self):
        self.number = 1
        self.string = "aaa"
        self.invalid_value = -500

    def test__method_value_error(self):
        self.assertEqual(find_the_lower_square("aaa"), None)

    def test_start_function(self):
        self.assertRaises(ValueError, start_function(self.string))

    def tearDown(self):
        pass
