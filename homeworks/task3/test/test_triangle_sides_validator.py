from unittest import TestCase
from homeworks.task3.app.main_triangles import is_triangle, Triangle

__author__ = 'nshumakov'


class TestTriangle(TestCase):
    def setUp(self):
        self.null = 0
        self.side_of_triangle = 4
        self.test_triangle = Triangle("first", 1, 1, 1)

    def test_sides_validator_one(self):
        self.assertTrue(is_triangle(self.side_of_triangle,
                                    self.side_of_triangle,
                                    self.side_of_triangle))

    def test_sides_validator_two(self):
        self.assertFalse(is_triangle(self.null, self.null, self.null))

    def test_triangle_square_function(self):
        self.assertGreater(self.test_triangle.calculate_area(), 0)

    def tearDown(self):
        print("Test passed")
