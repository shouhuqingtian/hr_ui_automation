# -*- coding: utf-8 -*-
# @Time    : 2024/8/12
# @Author  : Bin
# @Software: PyCharm
# @File    : test01.py
import time

str1 = 'hello'


# with open('output.txt', 'w') as f:
#     print('hello world!', file=f)
# print(str1)


def function():
    pass


class MyClass:
    def __init__(self, value):
        self.value = value  # 实例属性

    def method(self):
        return "This is a method"

    def __hidden_method(self):
        return "This is a hidden method"


# 创建类的实例
obj = MyClass(42)

# 使用 dir() 获取所有属性和方法
attributes = dir(obj)

# # 区分属性和方法
# for attr in attributes:
#     attr_value = getattr(obj, attr)
#     print(attr_value)
#     if callable(attr_value):
#         print(f"{attr} is a method.")
#     else:
#         print(f"{attr} is an attribute with value: {attr_value}")
num = [1, 2, 3, 4, 5]


# print(len(str1))


def greet(self):
    return f'hello, where are you from? {self.test01}'


t = type('test', (), {'test01': '01', 'greet': greet})
T = t()
# print(T.test01)
# print(T.greet())
# print(type(T))

my_gen = (i for i in range(10))

from collections.abc import Generator

# print(isinstance(my_gen, Generator))
test_str = "hello world!"

with open(file='TestFile.txt', mode='w') as f:
    f.write(test_str)

# import tkinter as tk
#
# root = tk.Tk()
# root.title("Simple GUI")
# label = tk.Label(root, text="Hello, World!")
# label.pack()
# root.mainloop()
#
# import tkinter
# from tkinter.constants import *
#
# tk = tkinter.Tk()
# frame = tkinter.Frame(tk, relief=RIDGE, borderwidth=2)
# frame.pack(fill=BOTH, expand=1)
# label = tkinter.Label(frame, text="Hello, World")
# label.pack(fill=X, expand=1)
# button = tkinter.Button(frame, text="Exit", command=tk.destroy)
# button.pack(side=BOTTOM)
# tk.mainloop()
