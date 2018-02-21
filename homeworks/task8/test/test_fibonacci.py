from unittest import TestCase
from homeworks.task8.app.fibonacci import fibonacci_counting

__author__ = 'nshumakov'


class TestFibonacciCounting(TestCase):
    def setUp(self):
        self.args_arr = [0, 1]

    def test_fibonacci_counting(self):
        self.assertEqual(fibonacci_counting(self.args_arr[0],
                                            self.args_arr[1]), self.args_arr)

    def test_not_in(self):
        self.assertNotIn(fibonacci_counting(self.args_arr[0],
                                            self.args_arr[1]), self.args_arr)

    def test_not_none(self):
        self.assertIsNotNone(fibonacci_counting(self.args_arr[0],
                                                self.args_arr[1]),
                             self.args_arr)

    def tearDown(self):
        pass
