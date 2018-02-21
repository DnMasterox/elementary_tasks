__author__ = 'nshumakov'


class ChessBoard(object):
    """

    Class ChessBoard

    """

    def __init__(self, height, width):
        self.__height = int(height)
        self.__width = int(width)

    def show_board(self, board_array) -> None:
        """

        :param board_array: array which contains presentation of board in a
            [*_*_] view
        :return: console view of board without []

        """
        for row in board_array:
            print(''.join([elem for elem in row]))

    def generate_board(self) -> []:
        """

        :return: array which contains presentation of board in a [*_*_] view

        """
        try:
            board_array = [[0] * self.__width for _ in range(self.__height)]
        except ValueError:
            return ValueError
        for i in range(self.__height):
            for j in range(self.__width):
                if i % 2 == 0:
                    if j % 2 == 1:
                        board_array[i][j] = '_'
                    else:
                        board_array[i][j] = '*'
                else:
                    if j % 2 == 1:
                        board_array[i][j] = '*'
                    else:
                        board_array[i][j] = '_'

        return board_array
