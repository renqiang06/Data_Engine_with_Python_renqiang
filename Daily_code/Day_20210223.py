#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# @Author  :   Ren Qiang
# %% 删除重复2次以上的元素
from collections import Counter as ct


def removeDuplicates(data: list) -> list:
    output = data[::-1]
    count = ct(data)
    for i in [k for k, v in count.items() if v > 2]:
        for _ in range(count[i]-2): # 需删除的次数
            output.remove(i)
    print(output[::-1])
    return output[::-1]


if __name__ == '__main__':
    input = [[1, 1, 1, 2, 2, 3],
             [1, 2, 2, 3, 5, 2, 4, 5, 3, 2, 1, 5],
             [3, 2, 2, 1]]
    result = list(map(removeDuplicates, input))
# %% 删除重复2次以上的元素
'''
from collections import Counter as ct
def removeDuplicates2(data: list) -> list:
    output = data[::-1]
    count = ct(data)
    for i in count.keys():
        num = count[i]
        while num > 2:
            output.remove(i)
            num -= 1
    print(output[::-1])
    return output[::-1]


if __name__ == '__main__':
    input = [[1, 1, 1, 2, 2, 3],
             [1, 2, 2, 3, 5, 2, 4, 5, 3, 2, 1, 5],
             [3, 2, 2, 1]]
    result = list(map(removeDuplicates2, input))
# %%
from collections import Counter as ct

def removeDuplicates3(data: list) -> list:
    output = []
    for i in data:
        if ct(output)[i] < 2:
            output.append(i)
    print(output)
    return output


if __name__ == '__main__':
    input = [[1, 1, 1, 2, 2, 3],
             [1, 2, 2, 3, 5, 2, 4, 5, 3, 2, 1, 5],
             [3, 2, 2, 1]]
    result = list(map(removeDuplicates3, input))
'''
