#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# @Author  :   Ren Qiang
# %% 求待插入的位置 二分法
'''
def searchInsert(num: list, target: int) -> int:
    start, end = 0, len(num)-1
    while start <= end:
        p = (start + end)//2
        if target < num[p]:
            end = p - 1
        elif num[p] < target:
            start = p + 1
            p += 1
        else:
            break
    print(p)
    return p


arr = [1, 3, 5, 6]
key = [5, 2, 7, 0]
for i in key:
    searchInsert(arr, i)
'''
# %% 求待插入的位置 一次二分
def searchInsert(num: list, target: int) -> int:
    num.sort()
    p = len(num)//2
    while p > 0 and p < len(num)-1:
        if num[p] > target:
            p -= 1
        elif num[p] < target:
            p += 1
        else:
            break
    if num[p] < target:
        p += 1
    print(p)
    return p


arr = [1, 3, 5, 6]
key = [5, 2, 7, 0]
for i in key:
    searchInsert(arr, i)
