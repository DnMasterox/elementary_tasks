from unittest import TestCase
from homeworks.task5.num2words.nums_to_words import NumberToWord

__author__ = 'nshumakov'


class TestNumToWord(TestCase):
    def setUp(self):
        self.num = NumberToWord()

    def test_int_to_word(self):
        self.assertEqual(
            self.num._int2word(215461407892039002157189883901676),
            "двести пятнадцать нониллионов четыреста шестьдесят один "
            "октиллион четыреста семь септиллионов восемьсот девяносто "
            "два секстиллиона тридцать девять квинтиллионов два квадриллиона "
            "сто пятьдесят семь триллионов сто восемьдесят девять миллиардов "
            "восемьсот восемьдесят три миллиона девятьсот одна тысяча "
            "шестьсот семьдесят шесть")

    def test_split_by_x(self):
        self.assertEqual(list(self.num._split_by_x(str(1234), 3)), [1, 234])

    def tearDown(self):
        pass
