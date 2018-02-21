from unittest import TestCase
from homeworks.task1.app.chessboard import ChessBoard

__author__ = 'nshumakov'


class TestChessBoard(TestCase):
    def setUp(self):
        test_value = 1
        self.test_feedback_result = [['*']]
        self.test_show_result = ['*']
        self.chessboard = ChessBoard(test_value, test_value)

    def test__draw_method(self):
        self.assertEqual(self.chessboard.generate_board(),
            self.test_feedback_result)

    def test__show_board(self):
        self.assertEqual(self.chessboard.show_board(self.test_show_result),
                         None)

    def tearDown(self):
        print("OK")
