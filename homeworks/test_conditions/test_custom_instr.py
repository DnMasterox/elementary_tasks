from unittest import TestCase
from homeworks.conditions.instructions import is_not_empty

__author__ = 'nshumakov'


class TestInstructions(TestCase):
    def setUp(self):
        self.empty_string = ""
        self.null = 0

    def test_is_empty(self):
        self.assertFalse(is_not_empty(self.empty_string, self.empty_string))
        self.assertTrue(is_not_empty(self.null, self.empty_string))

    def tearDown(self):
        pass
