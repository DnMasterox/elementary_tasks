__author__ = 'nshumakov'
from homeworks.conditions.validation import is_validated


class HappyTicketsCounter(object):
    def __init__(self):
        self.__max_tickets_number = 999999
        self.__sum_of_numbers_one = 0
        self.__sum_of_numbers_two = 0

    def print_all_moscow(self) -> None:
        print(self.get_all_moscow(self.__max_tickets_number))

    def print_all_peter(self) -> None:
        print(self.get_all_peter(self.__max_tickets_number))

    def get_all_moscow(self, max_tickets_number) -> int:
        if is_validated(max_tickets_number) and \
                        str(max_tickets_number).__len__() < 7:
            moscow_algorithm_counter = 0
            while max_tickets_number >= 0:
                tickets_list = list(str(max_tickets_number))
                max_tickets_number -= 1
                for _ in range(tickets_list.__len__()):
                    if int(_) % 2 == 0:
                        self.__sum_of_numbers_one += int(tickets_list[_])
                    else:
                        self.__sum_of_numbers_two += int(tickets_list[_])

                if self.__sum_of_numbers_one == self.__sum_of_numbers_two:
                    moscow_algorithm_counter += 1
                else:
                    pass
                    self.__sum_of_numbers_one, self.__sum_of_numbers_two \
                        = 0, 0
            return moscow_algorithm_counter
        else:
            raise ValueError("Incorrect values was entered")

    def get_all_peter(self, max_tickets_number) -> int:
        if is_validated(max_tickets_number) and str(max_tickets_number) \
                .__len__() < 7:
            peter_algorithm_counter = 0
            while max_tickets_number >= 0:
                right_side = max_tickets_number % 1000
                left_side = max_tickets_number // 1000
                max_tickets_number -= 1
                while int(right_side) != 0:
                    self.__sum_of_numbers_one += int(right_side % 10)
                    right_side /= 10
                while int(left_side) != 0:
                    self.__sum_of_numbers_two += int(left_side % 10)
                    left_side /= 10
                if self.__sum_of_numbers_one == self.__sum_of_numbers_two:
                    peter_algorithm_counter += 1
                else:
                    pass
                self.__sum_of_numbers_one, self.__sum_of_numbers_two = 0, 0

            return peter_algorithm_counter
        else:
            raise ValueError("Incorrect values was entered")
