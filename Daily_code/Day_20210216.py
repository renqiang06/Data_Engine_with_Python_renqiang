#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# @Author  :   Ren Qiang
# %% 数字的英文字母排序
from pandas import DataFrame as df


def number2Words(num: int) -> str:
    to19 = 'One Two Three Four Five Six Seven Eight Nine Ten '\
        'Eleven Twelve Thirteen Fourteen Fifteen Sixteen Seventeen Eighteen Nineteen'.split()
    tens = 'Twenty Thirty Forty Fifty Sixty Seventy Eighty Ninety'.split()
    thousand = 'Thousand Million Billion'.split()

    def word(num, n=0):
        if num == 0:
            return []
        elif num < 20:
            return [to19[num-1]]
        elif num < 100:
            return [tens[num//10-2]] + word(num % 10)
        elif num < 1000:
            return [to19[num//100-1]] + ['Hundred'] + word(num % 100)
        p, r = num//1000, num % 1000
        space = [thousand[n]] if p % 1000 != 0 else []
        return word(p, n+1) + space + word(r)
    return ' '.join(word(num)) or 'Zero'


def sort_by_name(arr):
    words = list(map(number2Words,arr)) # 调用转换函数
    data = {'数字': arr, '单词': words}
    Num_words = df(data).sort_values(by="单词")  # 按单词升序
    output = list(Num_words['数字'])  # 反馈排序后的数字
    print(output)
    return output


input = [[8, 8, 9, 9, 10, 10], [1, 2, 3, 4], [9, 99, 999], [0, 11, 222, 53, 40]]
result = list(map(sort_by_name, input))
# %%
'''
def number2Words(num: int) -> str:
    to19 = 'One Two Three Four Five Six Seven Eight Nine Ten '\
        'Eleven Twelve Thirteen Fourteen Fifteen Sixteen Seventeen Eighteen Nineteen'.split()
    tens = 'Twenty Thirty Forty Fifty Sixty Seventy Eighty Ninety'.split()

    def words(n):
        if n < 20:
            return to19[n-1:n]
        elif n < 100:
            return [tens[n//10-2]] + words(n % 10)
        elif n < 1000:
            return [to19[n//100-1]] + ['Hundred'] + words(n % 100)
        for p, w in enumerate(('Thousand', 'Million', 'Billion'), 1):
            if n < 1000**(p+1):
                return words(n//1000**p) + [w] + words(n % 1000**p)
    return ' '.join(words(num)) or 'Zero'


def sort_by_name(arr):
    words = []
    for i in arr:
        words.append(number2Words(i))  # 调用转换函数
    data = {'数字': arr, '单词': words}
    Num_words = df(data).sort_values(by="单词")  # 按单词升序
    output = list(Num_words['数字'])  # 反馈排序后的数字
    print(output)
    return output


input = [[8, 8, 9, 9, 10, 10], [1, 2, 3, 4],
         [9, 99, 999], [0, 11, 222, 53, 40]]
result = list(map(sort_by_name, input))
'''
# %%
'''
class Solution:
    def numberToWords(self, num):
        """
        :type num: int
        :rtype: str
        """
        def one(num):
            switcher = {
                1: 'One',
                2: 'Two',
                3: 'Three',
                4: 'Four',
                5: 'Five',
                6: 'Six',
                7: 'Seven',
                8: 'Eight',
                9: 'Nine'
            }
            return switcher.get(num)

        def two_less_20(num):
            switcher = {
                10: 'Ten',
                11: 'Eleven',
                12: 'Twelve',
                13: 'Thirteen',
                14: 'Fourteen',
                15: 'Fifteen',
                16: 'Sixteen',
                17: 'Seventeen',
                18: 'Eighteen',
                19: 'Nineteen'
            }
            return switcher.get(num)

        def ten(num):
            switcher = {
                2: 'Twenty',
                3: 'Thirty',
                4: 'Forty',
                5: 'Fifty',
                6: 'Sixty',
                7: 'Seventy',
                8: 'Eighty',
                9: 'Ninety'
            }
            return switcher.get(num)

        def two(num):
            if not num:
                return ''
            elif num < 10:
                return one(num)
            elif num < 20:
                return two_less_20(num)
            else:
                tenner = num // 10
                rest = num - tenner * 10
                return ten(tenner) + ' ' + one(rest) if rest else ten(tenner)

        def three(num):
            hundred = num // 100
            rest = num - hundred * 100
            if hundred and rest:
                return one(hundred) + ' Hundred ' + two(rest) 
            elif not hundred and rest: 
                return two(rest)
            elif hundred and not rest:
                return one(hundred) + ' Hundred'

        billion = num // 1000000000
        million = (num - billion * 1000000000) // 1000000
        thousand = (num - billion * 1000000000 - million * 1000000) // 1000
        rest = num - billion * 1000000000 - million * 1000000 - thousand * 1000

        if not num:
            return 'Zero'

        result = ''
        if billion:
            result = three(billion) + ' Billion'
        if million:
            result += ' ' if result else ''
            result += three(million) + ' Million'
        if thousand:
            result += ' ' if result else ''
            result += three(thousand) + ' Thousand'
        if rest:
            result += ' ' if result else ''
            result += three(rest)
        return result
'''
