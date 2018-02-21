"""
6. Happy tickets
Happy tickets.
There are 2 ways to calculate lucky tickets:

1. Moscow - if a six-figure number is printed on a bus ticket, and the sum of
    the first three digits is equal to the sum of the last three, then this
        ticket is considered to be happy.

2. Leningrad, or Petersburg - if the sum of even numbers of the ticket is
     equal to the sum of odd figures of the ticket,then the ticket is
        considered to be happy.


A task:
Ticket number is a six-digit number.
You need to write a console application that can calculate the number of
   lucky tickets.
To select a counting algorithm, a text file is read.
The path to the text file is set in the console after the program is
   started. Algorithm indicators:
1 - the word 'Moscow'
2 - the word 'Peter'
After setting all the necessary parameters, the program in the console
   should display the number of lucky tickets for the specified method of
      calculation.

"""

from homeworks.conditions.instructions import is_not_empty
from homeworks.task6.app.happy_tickets import HappyTicketsCounter

__author__ = 'nshumakov'

INSTRUCTIONS = "For correct work of this program,enter the path to file " \
               "please"
MOSCOW = "Moscow"
PETER = "Peter"


def start_function(params_to_start) -> None:
    """

    :param params_to_start: path to file
    :return:

    """
    try:
        with open(params_to_start, 'r') as file:
            array = str([row.strip() for row in file])
            happy_tickets_counter = HappyTicketsCounter()
            if MOSCOW in array:
                happy_tickets_counter.print_all_moscow()
            elif PETER in array:
                happy_tickets_counter.print_all_peter()
            else:
                pass

    except FileNotFoundError:
        print("Sorry, incorrect pass to file was entered. File not found")


if __name__ == '__main__':
    print("Enter the path to file please")
    input_param = input()
    if is_not_empty(input_param, INSTRUCTIONS):
        start_function(input_param)
    else:
        quit()
