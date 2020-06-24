# -*- coding: utf-8 -*-

import os
import sys
# import datetime
import logging
# import argparse
# from tqdm import tqdm
# import time
####################
# [modules]
# import modules.Program as pr
# from modules.Program import *

from modules import Module_Logging
# from modules import Module_Datetime
sys.path.append(os.path.dirname(__file__))
####################
# [logging]
# if not log.exist() mkdir 'tmp'
# logging.basicConfig(filename='tmp/logger.log', level=logging.DEBUG)
logging.basicConfig(level=logging.INFO)
Module_Logging.LogTest()
####################
# [argparse]
# psr = argparse.ArgumentParser()
# psr.add_argument('-w', '--word', default='words #')
# psr.add_argument('-s', '--size', default=3, type=int)
# args = psr.parse_args()
# print(args.word * args.size)
####################
# [progress-bar]
# for i in tqdm(range(100)):
# time.sleep(0.02)
####################


class outputClass:
    def __init__(self):
        """constructor
        """
        # CONST
        self._save_msg = "save"
        self._joined_args = ""

    def createMessage(self, *args):
        """date + args
        """
        self._joined_args = ' '.join(map(str, [' args =>'] + list(args)))

    def savedFile(self):
        """saveLog
        """
        logging.info(self._joined_args)

        # output
        # with open('.\log.txt', 'at') as fd: fd.write(msg + '\n')

##############################

# def __init__(self, int_id: int, str_name: str)
# self.__id: int = int_id
# self.__name: str = str_name

# @property
# def name(self) -> str:
#     return self.__name


class TestClass:
    """
    pythonではprivateな変数、変更不可な変数は存在しないようです。
    privateに関しては、「_」で始まる変数、メソッドはプライベートだという慣習はあるみたいです。
    """
    cl_v = "public or default_val"
    arr_args = []

    def __init__(self, val1, val2):
        """args test
        """
        self.arr_args.append(val1)
        self.arr_args.append(val2)

    def __del__(self):
        """destructor
        """


def main():
    """entry
    """
    oc = outputClass()
    oc.createMessage('val0', 'val1', 'val2')
    oc.savedFile()
    del oc

    tc = TestClass(1, 2)
    logging.info(tc.arr_args)
    del tc
    logging.info(TestClass.cl_v)


if __name__ == '__main__':
    main()

##############################


class Student:
    def __init__(self, name, school):
        self.name = name
        self.school = school
        self.marks = []

    def average(self):
        """
        @return marks
        """
        return sum(self.marks) / len(self.marks)

    @classmethod
    def friend(cls, origin, friend_name, *args):
        """add friend
        継承クラスで動作が変わるべき(継承クラスではsalaryプロパティがある)
        なのでclassmethodを使う。
        子クラスの初期化引数は *argsで受けるのがいい
        """
        return cls(friend_name, origin.school, *args)

    @staticmethod
    def say_hello():
        """共通処理
        継承しても同じ動きでいいのでstaticmethodを使う
        """


class WorkingStudent(Student):
    def __init__(self, name, school, salary):
        super().__init__(name, school)
        self.salary = salary


hiro = WorkingStudent("hiro", "stanford", 20.00)
mitsu = WorkingStudent(hiro, "Mitsu", 15.00)
print(mitsu.salary)
##############################
