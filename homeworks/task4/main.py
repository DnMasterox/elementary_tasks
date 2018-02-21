"""
4. File parser
You need to write a program that will have two modes:
1. Read the number of occurrences of a string in a text file.
2. Replace the string with another in the specified file
The program must accept input arguments at startup:
1. <path to file> <string for counting>
2. <path to file> <string to search> <string to replace>
"""

from homeworks.task4.file_handlers import FileStringFinder
from homeworks.task4.file_handlers import FileStringReplacer
from homeworks.conditions.instructions import is_not_empty

__author__ = 'nshumakov'

INSTRUCTIONS = "Choose mode and enter the values: " "\n" \
               "1.<Way to file> <line to count> ""\n" \
               "2.<Way to file> <line to search> <line to replace>""\n"


def start_function(params_to_start) -> None:
    """

    if params_to_start length will be 2 FileStringFinder(counter) will start
    if params_to_start length will be 3 FileStringReplacer will start
    :param params_to_start: array with parameters to start work of the program

    """
    try:
        if params_to_start.__len__() == 2:
            file_string_finder = FileStringFinder(params_to_start[0],
                                                  params_to_start[1])
            file_string_finder.print_occurrences()
        elif params_to_start.__len__() == 3:
            FileStringReplacer(params_to_start[0],
                               params_to_start[1],
                               params_to_start[2])
        else:
            pass
    except FileNotFoundError:
        print("Sorry but the File have not been found")


def string_to_list(string) -> list:
    """

    clean the entered data
    :param string: entered data
    :return: list with parameters
    """
    try:
        string = string.replace('>', '')
        string = string.replace('<', '')
        string = string.replace(' ', ',')
        param_list = [x for x in string.split(',')]
        if param_list.__len__() < 2 or param_list.__len__() > 3:
            print("Incorrect data was entered!")
            quit()
        else:
            return param_list
    except TypeError:
        print(str(TypeError))


if __name__ == '__main__':
    print("Choose mode and enter the values: " "\n"
          "1.<Way to file> <line to count> ""\n"
          "2.<Way to file> <line to search> <line to replace>""\n")
    input_data = input()
    if is_not_empty(input_data, INSTRUCTIONS):
        start_function(string_to_list(input_data))
    elif "<>" not in input_data:
        print("Please enter correct values")
    else:
        quit()
