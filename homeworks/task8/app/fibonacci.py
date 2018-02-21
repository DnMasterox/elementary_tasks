"""

8. Fibonacci series for the range
The program allows you to output all Fibonacci numbers that are in the
    specified range.
The range is specified by two arguments when the main class is called.
The numbers are output comma-separated in ascending order.

"""
from homeworks.conditions.instructions import is_not_empty
from homeworks.conditions.validation import is_validated_fibonacci

__author__ = 'nshumakov'

INSTRUCTION = "For correct working of this program, you must enter 2 " \
              "Integer values - start and end of sequence!"


def fibonacci_counting(number_one, number_two) -> []:
    """

    :param number_one: start of sequence
    :param number_two: end of sequence
    :return: array with counted fibonacci line

    """
    array_fibonacci_results = []
    try:
        number_one = min(float(number_one), float(number_two))
        max_value = max(float(number_one), float(number_two))
    except ValueError:
        print("Entered values is incorrect")
    if number_one == 0:
        number_two = number_one + 1
    else:
        number_two = number_one
    array_fibonacci_results.append(number_one)
    array_fibonacci_results.append(number_two)
    while number_one + number_two < max_value:
        fibonacci_number = number_one + number_two
        array_fibonacci_results.append(fibonacci_number)
        number_one, number_two = number_two, fibonacci_number
    return array_fibonacci_results


def array_presenting(array) -> None:
    for number in array:
        print(int(number))


if __name__ == '__main__':
    start_of_sequence = input('Please enter the first member of sequence' +
                              '\n')
    if is_not_empty(start_of_sequence, INSTRUCTION) and \
            is_validated_fibonacci(start_of_sequence):
        end_of_sequence = input('Please enter the second member of sequence'
                                + '\n')
        if is_not_empty(end_of_sequence, INSTRUCTION) and \
                is_validated_fibonacci(end_of_sequence):
            fibonacci_in_sequence = fibonacci_counting(start_of_sequence,
                                                       end_of_sequence)
            array_presenting(fibonacci_in_sequence)
        else:
            quit()
    else:
        quit()
