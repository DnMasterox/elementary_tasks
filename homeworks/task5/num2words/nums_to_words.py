__author__ = 'nshumakov'

ZERO = ('ноль',)

ONES_FEMININE = {
    1: ('одна',),
    2: ('две',),
    3: ('три',),
    4: ('четыре',),
    5: ('пять',),
    6: ('шесть',),
    7: ('семь',),
    8: ('восемь',),
    9: ('девять',),
}

ONES = {
    1: ('один',),
    2: ('два',),
    3: ('три',),
    4: ('четыре',),
    5: ('пять',),
    6: ('шесть',),
    7: ('семь',),
    8: ('восемь',),
    9: ('девять',),
}

TENS = {
    0: ('десять',),
    1: ('одиннадцать',),
    2: ('двенадцать',),
    3: ('тринадцать',),
    4: ('четырнадцать',),
    5: ('пятнадцать',),
    6: ('шестнадцать',),
    7: ('семнадцать',),
    8: ('восемнадцать',),
    9: ('девятнадцать',),
}

TWENTIES = {
    2: ('двадцать',),
    3: ('тридцать',),
    4: ('сорок',),
    5: ('пятьдесят',),
    6: ('шестьдесят',),
    7: ('семьдесят',),
    8: ('восемьдесят',),
    9: ('девяносто',),
}

HUNDREDS = {
    1: ('сто',),
    2: ('двести',),
    3: ('триста',),
    4: ('четыреста',),
    5: ('пятьсот',),
    6: ('шестьсот',),
    7: ('семьсот',),
    8: ('восемьсот',),
    9: ('девятьсот',),
}

THOUSANDS = {
    1: ('тысяча', 'тысячи', 'тысяч'),  # 10^3
    2: ('миллион', 'миллиона', 'миллионов'),  # 10^6
    3: ('миллиард', 'миллиарда', 'миллиардов'),  # 10^9
    4: ('триллион', 'триллиона', 'триллионов'),  # 10^12
    5: ('квадриллион', 'квадриллиона', 'квадриллионов'),  # 10^15
    6: ('квинтиллион', 'квинтиллиона', 'квинтиллионов'),  # 10^18
    7: ('секстиллион', 'секстиллиона', 'секстиллионов'),  # 10^21
    8: ('септиллион', 'септиллиона', 'септиллионов'),  # 10^24
    9: ('октиллион', 'октиллиона', 'октиллионов'),  # 10^27
    10: ('нониллион', 'нониллиона', 'нониллионов'),  # 10^30
}


class NumberToWord(object):
    def __init__(self, number_to_words=0):
        self.__number = int(number_to_words)

    def print_word(self) -> None:
        print(self._int2word(self.__number))

    def _pluralize(self, remainder, forms) -> str:
        """

        :param remainder:remainder from division
        :param forms: inclined array
        :return:decline
        """
        if remainder % 100 < 10 or remainder % 100 > 20:
            if remainder % 10 == 1:
                form = 0
            elif 5 > remainder % 10 > 1:
                form = 1
            else:
                form = 2
        else:
            form = 2
        return forms[form]

    def _int2word(self, entered_number, feminine=False) -> []:
        if int(entered_number) == 0:
            return ZERO[0]
        else:
            words_to_print = []
            parts = list(self._split_by_x(str(entered_number), 3))
            i = len(parts)
            for part in parts:
                i -= 1
                n1, n2, n3 = self._get_digits(part)

                if n3 > 0:
                    words_to_print.append(HUNDREDS[n3][0])
                else:
                    pass

                if n2 > 1:
                    words_to_print.append(TWENTIES[n2][0])
                else:
                    pass

                if n2 == 1:
                    words_to_print.append(TENS[n1][0])
                elif n1 > 0:
                    if i == 1 or feminine and i == 0:
                        ones = ONES_FEMININE
                    else:
                        ones = ONES
                    words_to_print.append(ones[n1][0])

                if i > 0 and part != 0:
                    words_to_print.append(self._pluralize(part, THOUSANDS[i]))
            return ' '.join(words_to_print)

    def _split_by_x(self, number, separating_length, format_int=True):
        """

        :param number:
        :param separating_length:
        :param format_int:
        :return:
        """
        all_length = len(number)
        if all_length > separating_length:
            start = all_length % separating_length
            if start > 0:
                result = number[:start]
                yield int(result) if format_int else result
            for i in range(start, all_length, separating_length):
                result = number[i:i + separating_length]
                yield int(result) if format_int else result
        else:
            yield int(number) if format_int else number

    def _get_digits(self, number) -> []:
        """

        separating number to 3 digits
        :param number: entered number
        :return:list with separated digits reversed

        """
        array_of_digits = [int(digit) for digit in reversed(list(
            ('%03d' % number)[-3:]))]
        return array_of_digits
