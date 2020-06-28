#!/.venv/Scripts python
# /usr/bin/env python
# -*- coding: utf-8 -*-
####################

# from django.conf import settings
# from django.core.mail import EmailMessage
####################
import os
import sys
import re

# pass
import hashlib
import uuid

# module
# import numpy as np
import django

# import matplotlib.pyplot as plt

# import pytest


def print_about():
    """print about"""
    # python version
    print("sys.version: " + sys.version.split()[0])
    # cwd
    print("cwd: " + os.getcwd())

    # add .env DEBUG=1
    # source .venv/Scripts/activate
    # pipenv shell
    # print(os.environ)
    print("env(debug): " + str(os.getenv("DEBUG")))
    # print("env(secret_key): " + str(os.getenv("SECRET_KEY")))

    # django
    print("django: " + django.__version__)


def print_args():
    """pipfile
    [script] pfArgs = "python test_about.py"
    $ pipenv run pfArgs [arg1 arg2 arg3]
    """
    args = ", ".join(sys.argv)
    print("pfArgs: " + args)


def print_regex():
    if re.match("abcde", "abcde"):
        print("match")  # -> "match"

    m = re.findall("c", "abcde")
    print(m)  # -> ['', '', '', '', '', '']


def gen_pass():
    salt = uuid.uuid4().hex
    password = "aa"
    hashed_password = hashlib.sha256(password + salt).hexdigest()
    print(hashed_password)


####################


def render_sin():
    """import numpy, matplotlib"""
    print("numpy: " + np.__version__)

    x = np.linspace(-np.pi, np.pi)
    y = np.sin(x)
    plt.plot(x, y)
    plt.show()


####################
# ファイル: pytest test/test_foo.py
# 関数: pytest test/test_foo.py::test_function
# クラス: pytest test/test_foo.py::TestClass
# クラスのメソッド: pytest test_foo.py::TestClass::test_method

# xunit
# class FooTest(TestCase):
#     def test_function(self):
#         self.assertEquals(f(), 4)

# pytest
# def test_function():
#     assert f() == 4


def f(n):
    return n * 1


def test_f():
    n = 3
    # assert f() == 3
    assert len(f(n)) >= n, "返された値が要求数より少ない"


####################
# pytest --doctest-modules

# export PYTEST_ADDOPTS='-v -s --pdb --ff --doctest-modules' # おすすめ！
# pytest # PYTEST_ADDOPTS が自動で付加されて実行

####################
# pytest --cov=mypkg --cov-report=html # mypkg のカバレッジを測定する

# pytest --junitxml=path
# JUnit形式はテスト結果ファイルのデファクトスタンダードであり、JenkinsやGitlabなどのツールで集計できたりします。
####################
# def test_raises():
#     with pytest.raises(ZeroDivisionError):
#         1 / 0


# def test_match():
#     with pytest.raises(ValueError, match=r".* 123 .*"):
#         raise ValueError("Exception 123 raised")


# def test_excinfo():
#     with pytest.raises(RuntimeError) as excinfo:
#         raise RuntimeError("ERROR")
#     assert str(excinfo.value) == "ERROR"
####################


# @pytest.fixture
# def smtp():
#     import smtplib

#     return smtplib.SMTP("smtp.example.com")


# @pytest.fixture
# def imap():
#     import imaplib

#     return imaplib.IMAP4("imap.example.com")


# def test_foo(smtp, imap):
#     """smtp と imap を使ったテスト"""


####################
# class TestClasss:

# def test_1(self):
#     x = "this"
#     assert "h" in x

# def test_2(self):
#     assert hasattr(x, "check")


####################


####################


def main():
    """entry"""
    # about
    print_about()

    # pipfile args
    # print_args()

    # module
    # render_sin()


if __name__ == "__main__":
    main()
