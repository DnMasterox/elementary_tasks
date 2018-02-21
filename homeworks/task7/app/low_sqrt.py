"""
7. A numerical sequence
The program displays a series of natural numbers separated by a comma,
the square of which is less than the given number n.
The program is launched via the main class call with parameters.

"""

from homeworks.conditions.instructions import is_not_empty
from homeworks.conditions.validation import is_validated

__author__ = 'nshumakov'

INSTRUCTION = "For correct working of this program, you must enter Integer " \
              "value!"


def start_function(data) -> None:
    try:
        print(find_the_lower_square(data))

    except ValueError:
        return ValueError


def find_the_lower_square(data) -> []:
    try:
        if int(data) < 0:
            raise ArithmeticError
        else:
            iterator = 0
            array_of_squares = []

            while iterator * iterator < int(data):
                array_of_squares.append(iterator)
                iterator += 1
            return ','.join([str(i) for i in array_of_squares])
    except ValueError:
        print(ValueError)
    except TypeError:
        return TypeError


if __name__ == '__main__':
    print("Please enter the the number!")
    entered_number = input()
    if is_not_empty(entered_number, INSTRUCTION) and is_validated(
            entered_number):
        start_function(entered_number)
    else:
        quit()
