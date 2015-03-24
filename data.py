# -*- coding: utf-8 -*-
import string
from datetime import datetime
from random import SystemRandom, choice


class RandomData(object):
    sys_random = SystemRandom()
    numbers = ''.join(map(str, range(10)))
    letters = string.letters
    letter_and_digit = '%s%s' % (string.letters, string.digits)

    @staticmethod
    def get_int(start=0, stop=10, step=1):
        return RandomData.sys_random.randrange(start, stop, step)

    @staticmethod
    def get_number(length=1):
        ret = []
        for i in range(length):
            ret.append(choice(RandomData.numbers))
        return ''.join(ret)

    @staticmethod
    def get_letter(length=1):
        ret = []
        for i in range(length):
            ret.append(choice(RandomData.letters))
        return ''.join(ret)

    @staticmethod
    def get_letter_digit(length=1):
        ret = []
        for i in range(length):
            ret.append(choice(RandomData.letter_and_digit))
        return ''.join(ret)

    @staticmethod
    def random_choice(seq):
        return choice(seq)

    @staticmethod
    def current_year():
        return datetime.now().strftime("%Y")

    @staticmethod
    def current_month():
        return datetime.now().strftime("%m")

    @staticmethod
    def current_day():
        return datetime.now().strftime("%d")

    @staticmethod
    def current_weekday():
        return datetime.now().weekday() + 1
