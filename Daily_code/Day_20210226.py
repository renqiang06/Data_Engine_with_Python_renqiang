#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = 'Ren Qiang'
# %% 串联单词的子串 前提：单词长度相等


def findSubstring(s: str, words: list) -> list:
    output = []
    L0 = len(words[0])
    for i in range(len(s)-len(words)*L0+1):
        temp, j= words[:], i
        while s[j:j+L0] in temp:
            temp.remove(s[j:j+L0])
            if not temp:
                output.append(i)
                break
            j += L0
    print(output)
    return output


if __name__ == '__main__':
    s = ['barfoothefoobarman', 'wordgoodgoodgoodbestword']
    w = [['foo', 'bar'], ['word', 'good', 'best', 'word'],
               ['good', 'best', 'word']]
    findSubstring(s[0], w[0])
    findSubstring(s[1], w[1])
    findSubstring(s[1], w[2])
