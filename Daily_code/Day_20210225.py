#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = 'Ren Qiang'
# %% 汉明距离


def hanmingDistance(nums: list) -> int:
    # c1 = bin(nums[0])
    # c2 = bin(nums[1])
    # c3 = nums[0] ^ nums[1]
    calc = bin(nums[0] ^ nums[1])
    output = calc.count('1')
    print(output)
    return output


if __name__ == '__main__':
    input = [[1, 4], [20, 34], [55, 34], [78, 96], [1278, 196]]
    result = list(map(hanmingDistance, input))
# %% 汉明距离

'''
def hanmingDistance2(nums: list) -> int:
    # c1 = bin(nums[0])
    # c2 = bin(nums[1])
    # c3 = nums[0] ^ nums[1]
    calc = bin(nums[0] ^ nums[1])
    output = calc.count('1')
    print(output)
    return output


if __name__ == '__main__':
    input = [[1, 4], [20, 34], [55, 34],
             [78, 96], [1278, 196]]
    result = list(map(hanmingDistance2, input))
'''