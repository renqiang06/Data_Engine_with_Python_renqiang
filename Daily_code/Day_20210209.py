#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# @Author  :   Ren Qiang
# 编写duplicate_count(text),返回多次出现的字符的个数。
# 不区分大小写的字母字符和数字，输入只包含字母（大小写）和数字。
# %% 重复字符串的个数
from collections import Counter


def duplicate_count(text):
    text = text.upper()
    s = set(text)
    output = 0
    for i in s:
        if text.count(i) > 1:
            output += 1
    print(output)
    return output


input = ['abcde', 'aabBcde', 'indivisibility']  # 输入
result = list(map(duplicate_count, input))
print(result)
# %% 调包 counter


def duplicate_count_2(text):
    text = text.upper()
    b = dict(Counter(text))
    output = [key for key, value in b.items() if value > 1]
    print(len(output))
    return len(output)


input = ['abcde', 'aabBcde', 'indivisibility']  # 输入
result = list(map(duplicate_count_2, input))
# %% 删除重复值。循环次数=字符个数


def duplicate_count_3(text):
    text_up = text.upper()  # 转换为大写
    output = 0
    for i in text_up:
        # print(i)
        if text_up.count(i) > 1:
            text_up = text_up.replace(i, '')  # 删掉重复字符
            output += 1
            # print(i, 'in')
    print(text, '\t中重复字符的个数：', output)
    return output


input = ['abcde', 'aabBcde', 'indivisibility']  # 输入
result = list(map(duplicate_count_3, input))
# %% while 循环，循环次数=非重复字符数-1


def duplicate_count_4(text):
    text_up = text.upper()  # 转换为大写
    output, i = 0, 0
    while i < len(text_up)-1:  # 最后一个字符不需要判断
        if text_up.count(text_up[i]) > 1:
            text_up = text_up.replace(text_up[i], '')  # 删掉重复字符，减少while循环次数
            output += 1
            continue  # 跳过i+1步骤,再从上次循环位置取一个字符
        i += 1
    print(text, '\t中重复字符的个数：', output)
    return output


input = ['abcde', 'aabBcde', 'indivisibility']  # 输入
result = list(map(duplicate_count_4, input))
# %% 不指定循环次数


def duplicate_count_5(text):
    text_up = text.upper()  # 转换为大写
    output, i = 0, 0
    while 1:
        try:
            if text_up.count(text_up[i]) > 1:
                text_up = text_up.replace(text_up[i], '')  # 删掉重复字符，减少while循环次数
                output += 1
                continue  # 跳过i+1步骤,再从上次循环位置取一个字符
            i += 1
        except:
            break
    print(text, '\t中重复字符的个数：', output)
    return output


input = ['abcde', 'aabBcde', 'indivisibility']  # 输入
result = list(map(duplicate_count_5, input))

# %%


def duplicate_count_6(text):
    text = text.upper()
    count = 0
    for i in range(len(text)-1):
        for j in range(i+1, len(text)):
            if text[i] == text[j]:
                count += 1
                break
    print(count)
    return count


input = ['abcde', 'aabBcde', 'indivisibility']  # 输入
result = list(map(duplicate_count_6, input))

# %%
