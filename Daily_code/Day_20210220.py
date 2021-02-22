#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# @Author  :   Ren Qiang
# %% 猜数字
from random import randint as r
from pprint import pprint


def guessnum():
    i, num = 0, r(1, 100)
    print(num)
    while True:
        guess = int(input("\n请输入一个数字："))
        i += 1
        if guess > num:
            print('太大了，请重新输入')
        elif guess < num:
            print('太小了，请重新输入')
        else:
            str = ['恭喜你，猜中了！', '共猜了{}次'.format(i)]
            pprint(str, indent=2, width=10)
            break


guessnum()
# %%
