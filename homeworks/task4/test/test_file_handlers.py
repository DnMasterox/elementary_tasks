from unittest import TestCase
from homeworks.task4.file_handlers import FileStringFinder
from homeworks.task4.main import start_function, string_to_list

__author__ = 'nshumakov'


class TestFileStringFinder(TestCase):
    def setUp(self):
        self.test_string = "<>2 2"
        self.test_list = ['2', '2']
        self.file_string_finder = FileStringFinder("", "")

    def test_start_function_one(self):
        self.assertRaises(TypeError, start_function(self.test_string))

    def test_start_function_two(self):
        self.assertEqual(start_function(self.test_list), None)

    def test_string_to_list(self):
        self.assertEqual(string_to_list(self.test_string), self.test_list)

    def tearDown(self):
        print("Test passed")
