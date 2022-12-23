#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

"""
Напишите рекурсивную функцию, проверяющую правильность расстановки скобок в строке.
При правильной расстановке выполняются условия:
количество открывающих и закрывающих скобок равно.
внутри любой пары открывающая – соответствующая закрывающая скобка, скобки
расставлены правильно.
"""


def check_brackets(s):
    """ checks if brakcet expression is correct """
    left_bracket = s.find("(")
    right_bracket = s.rfind(")")

    if left_bracket == -1 and right_bracket == -1:
        return True
    elif left_bracket == -1 or right_bracket == -1 or right_bracket < left_bracket:
        return False
    else:
        return check_brackets(s[left_bracket+1:right_bracket])


if __name__ == '__main__':
    if check_brackets(input('Введите строку: ')):
        print('Correct brackets')
    else:
        print('Incorect brackets')