# -*- coding: utf-8 -*-
"""
Created on Wed Jan 27 14:50:34 2021

@author: RenQiang

Action1：求2+4+6+8+...+100的求和，用Python该如何写
"""
# 方法1 
# 列出数组
# a1 = list(range(2,101,2))
a = sum(range(2,101,2))
print(a)
# 方法2
# 构建循环
b=0
for i in range(2,101,2):
    b+=i
print(b)

# 方法3
# 数学计算等差数列
a1 = 2
an = 100
d = 2

n = (an-a1)/d+1
sn = n*(a1+an)/2
print(sn)