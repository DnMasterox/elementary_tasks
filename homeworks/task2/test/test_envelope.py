from unittest import TestCase
from homeworks.task2.app.envelope import Envelope

__author__ = 'nshumakov'


class TestEnvelope(TestCase):
    def setUp(self):
        self.envelope_a = Envelope(10, 10)
        self.envelope_b = Envelope(1, 1)
        self.envelope_c = self.envelope_a

    def test_compare_one(self):
        self.assertTrue(self.envelope_a.is_fitted(self.envelope_b))

    def test_compare_two(self):
        self.assertFalse(self.envelope_b.is_fitted(self.envelope_a))

    def test_compare_three(self):
        self.assertTrue(self.envelope_c.is_fitted(self.envelope_a))

    def tearDown(self):
        print("OK")
