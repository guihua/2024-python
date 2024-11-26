#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Student(object):
    def __init__(self, name, gender, score):
        # 私有变量，不能被外部访问, 也不能被外部修改
        self.__name = name
        self.__gender = gender
        self.__score = score

    # 定义方法，外部可以通过方法访问和修改私有变量
    def get_name(self):
        return self.__name

    # 定义方法，外部可以通过方法访问和修改私有变量
    def get_gender(self):
        return self.__gender

    def get_score(self):
        return self.__score

    def set_gender(self, gender):
        self.__gender = gender

    def set_score(self, score):
        # 定义方法，外部可以通过方法访问和修改私有变量, 并对输入进行判断
        if 0 <= score <= 100:
            self.__score = score
        else:
            raise ValueError('bad score')

    def get_grade(self):
        if self.__score >= 90:
            return 'A'
        elif self.__score >= 60:
            return 'B'
        else:
            return 'C'