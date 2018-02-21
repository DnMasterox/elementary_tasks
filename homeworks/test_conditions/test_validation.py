from unittest import TestCase
from homeworks.conditions.validation import is_validated, \
    is_validated_fibonacci

__author__ = 'nshumakov'


class TestValidation(TestCase):
    def setUp(self):
        self.positive_int = 10
        self.negative_int = -10
        self.null = 0
        self.test_string = "asf"
        self.test_object = object

    def test_validation_positive_int(self):
        self.assertTrue(is_validated(self.positive_int))

    def test_validation_negative_int(self):
        self.assertFalse(is_validated(self.negative_int))

    def test_validation_null(self):
        self.assertFalse(is_validated(self.null))

    def test_validation_string(self):
        self.assertFalse(is_validated(self.test_string))

    def test_validation_fibonacci(self):
        self.assertTrue(is_validated_fibonacci(self.null))

    def tearDown(self):
        pass
