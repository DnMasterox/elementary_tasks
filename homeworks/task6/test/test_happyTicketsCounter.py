from unittest import TestCase
from homeworks.task6.app.happy_tickets import HappyTicketsCounter
from homeworks.task6.app.main_happy_tickets import start_function


class TestHappyTicketsCounter(TestCase):
    def setUp(self):
        self.test_value = 111111
        self.test_string = "zasdfafs"
        self.happy_tickets_counter = HappyTicketsCounter()

    def test_get_all_moscow(self):
        self.assertGreater(self.happy_tickets_counter.get_all_moscow(
            self.test_value), 0)

    def test_get_all_peter(self):
        self.assertGreater(self.happy_tickets_counter.get_all_peter(
            self.test_value), 0)

    def test_start_function(self):
        self.assertFalse(start_function(self.test_string))
        # self.assertRaises(OSError)

    def tearDown(self):
        print("OK")
