"""
2. Analysis of envelopes
There are two envelopes with sides (a, b) and (c, d) to determine whether one
envelope can be put in another.
The program must handle the input of floating-point numbers.
The program asks the user for the size of the envelopes for one parameter at a
 time.
After each count, the program asks the user if they want to continue.
If the user answers "y" or "yes" (case-insensitive), the program continues to
work first,
otherwise it completes execution.
"""

from homeworks.conditions.instructions import is_not_empty
from homeworks.conditions.validation import is_validated
from homeworks.task2.app.envelope import Envelope

__author__ = 'nshumakov'

INSTRUCTION = "For correct working of this program, you must enter Float" \
              " values!"


def start_function() -> None:
    """

    check the entered values one by one. If "show_instructions" function will
    get empty string, it will return the
    "INSTRUCTION" if entered value will be positive it will pass the
    "validation_positive__int" the same manipulations
    will be done  to the next entered values, if it will pass validations
    function creates a class object

    :return:

    """
    a = input("Please enter the envelop side 'a'" + "\n")
    if is_not_empty(a, INSTRUCTION) and is_validated(a):
        b = input("Please enter the envelop side 'b'" + "\n")
        if is_not_empty(b, INSTRUCTION) and is_validated(b):
            envelope_first = Envelope(a, b)
            c = input("Please enter the envelop side 'c'" + "\n")
            if is_not_empty(c, INSTRUCTION) and is_validated(c):
                d = input("Please enter the envelop side 'd'" + "\n")
                if is_not_empty(d, INSTRUCTION) and is_validated(d):
                    envelope_second = Envelope(c, d)
                    if envelope_first.is_fitted(envelope_second):
                        print("Second envelope can fit into the first")
                    elif envelope_second.is_fitted(envelope_first):
                        print("First envelope can fit into the second")
                    else:
                        print("Fitting is impossible")
                else:
                    pass
            else:
                pass
        else:
            pass
    else:
        quit()


if __name__ == '__main__':
    start_function()
