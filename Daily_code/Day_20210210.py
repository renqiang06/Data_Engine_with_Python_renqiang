#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# @Author  :   Ren Qiang
# 广义斐波那契数列 Tribonacci(signature,n)
import numpy as np
# %% 循环往后累加, 循环次数=n-3


def Tribonacci(signature, n):
    x, y, z = signature  # 特定初始只有三位
    output = []
    if n > 2:
        output = signature
        for _ in range(n-3):
            x, y, z = y, z, x+y+z  # 迭代往后
            output.append(z)
    print(output)
    return output


input = [1, 1, 1]  # 输入
n = 10
result = Tribonacci(input, n)
# %%


def Tribonacci_2(signature, n):
    x, y, z = signature  # 特定初始只有三位
    output = []
    if n > 2:
        for _ in range(n):
            output.append(x)
            x, y, z = y, z, x+y+z  # 迭代往后
    print(output)
    return output


input = [1, 1, 1]  # 输入
n = 10
result = Tribonacci_2(input, n)
# %% 矩阵


def Tribonacci_3(a, b, c, n):
    for i in range(n):
        q = pow((np.matrix([[1, 1, 1], [1, 0, 0], [0, 1, 0]])),
                i-2)*np.matrix([[c], [b], [a]])
        print(int(q[0][0]))


Tribonacci_3(1, 1, 1, 2)

# %%
