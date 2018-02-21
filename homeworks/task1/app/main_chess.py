"""

1. Chessboard
Bring out a chessboard with the given sizes of height and width, on a
   principle:
*  *  *  *  *  *
  *  *  *  *  *  *
*  *  *  *  *  *
  *  *  *  *  *  *

"""

from homeworks.conditions.instructions import is_not_empty
from homeworks.conditions.validation import is_validated
from homeworks.task1.app.chessboard import ChessBoard

__author__ = 'nshumakov'

INSTRUCTION = "For correct working of this program, you must enter 2 " \
              "Integer values!"


def start_function() -> None:
    """

    Function creates a class object, calls the method for creating an array,
       and displays the chessboard from the array
    :return:

    """
    try:
        chessboard = ChessBoard(height_of_board, width_of_board)
        chessboard_array = chessboard.generate_board()
        chessboard.show_board(chessboard_array)
    except ValueError:
        print(str(ValueError))


if __name__ == '__main__':
    print("Please enter the height of the desirable board!")
    height_of_board = input()

    # check the entered values. If "show_instructions" function will get empty
    # string, it will return the "INSTRUCTION"
    # if entered value will be positive it will pass the
    # "validation_positive__int" the same manipulations will be done
    # to the second entered value, if it will pass validations? start function
    # will be start

    if is_not_empty(height_of_board, INSTRUCTION) and \
            is_validated(height_of_board):
        print("Please enter the width of the desirable board!")
        width_of_board = input()
        if is_not_empty(width_of_board, INSTRUCTION) and \
                is_validated(width_of_board):
            start_function()
        else:
            quit()
    else:
        quit()
