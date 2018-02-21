class Envelope(object):
    """

    Envelope class

    """

    def __init__(self, side_a, side_b) -> None:
        self.__side_a = float(side_a)
        self.__side_b = float(side_b)

    def is_fitted(self, envelope) -> bool:
        """

        :param envelope: another envelope to comparing
        :return: True if second envelope will fit into the first and False
           if will not

        """
        min_side_one = self.get_min_side()
        min_side_two = envelope.get_min_side()
        max_side_one = self.get_max_side()
        max_side_two = envelope.get_max_side()

        if self.__is_larger(max_side_one, max_side_two) and \
                self.__is_larger(min_side_one, min_side_two):
            return True
        elif self.__is_larger(max_side_two, max_side_one) and \
                self.__is_larger(max_side_two,
                                 max_side_one):
            return False

    def __is_larger(self, float_one, float_two) -> bool:
        """

        :param float_one: the first value of comparing
        :param float_two: the second value of comparing
        :return: True - if float_one is bigger than float_two or the same and
           False if conversely

        """
        if float_one - float_two >= 0:
            return True
        else:
            return False

    def get_min_side(self) -> float:
        """

        :return: min side of this envelope

        """
        return min(self.__side_a, self.__side_b)

    def get_max_side(self) -> float:
        """

        :return:max side of this envelope

        """
        return max(self.__side_a, self.__side_b)
