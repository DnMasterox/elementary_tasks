"""
5. The number in the list
It is necessary to convert the whole number into a capital variant:
    12 - twelve.
The program is launched via the main class call with parameters.

"""

from homeworks.conditions.instructions import is_not_empty
from homeworks.conditions.validation import is_validated
from homeworks.task5.num2words.nums_to_words import NumberToWord

__author__ = 'nshumakov'

instruction = "For correct working of this program, you must enter Integer " \
              "values!"


def start_function(entered_number):
    if is_not_empty(entered_number, instruction) and \
            is_validated(entered_number):
        try:
            if str(entered_number).__len__() < 31:
                converted_number = NumberToWord(entered_number)
                converted_number.print_word()
            else:
                print("Sorry but entered number is too long")
        except ValueError:
            print("Incorrect value was entered")

    else:
        quit()


if __name__ == '__main__':
    entered_value = input("Please enter the positive number: " + "\n")
    start_function(entered_value)
