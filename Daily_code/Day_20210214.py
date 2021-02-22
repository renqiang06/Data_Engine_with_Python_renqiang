#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# @Author  :   Ren Qiang
# %% 验证优惠券代码是否有效
from datetime import datetime


def checkCoupon(entered_code, correct_code, current_date, expriration_date):
    T_0 = datetime.strptime(current_date, '%B %d, %Y')
    T_1 = datetime.strptime(expriration_date, '%B %d, %Y')
    output = entered_code == correct_code and T_0 <= T_1
    return output


print(checkCoupon('123', '123', 'September 5, 2014', 'October 1, 2014'))
print(checkCoupon('123a', '123', 'September 5, 2014', 'October 1, 2014'))
print(checkCoupon("123", "123", "July 9, 2015", "July 2, 2015"))
# %%
