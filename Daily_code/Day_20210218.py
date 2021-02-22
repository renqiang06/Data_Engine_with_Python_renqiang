#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# @Author  :   Ren Qiang
# %% 最长回文子串
def longest_palindrome(s: str) -> int:
    output = 1
    for i in range(len(s)-1):
        j, k = 0, 0
        if len(s) > 1 and i-j >= 0 and i+j+1 <= len(s)-1:
            while s[i-j] == s[i+j+1]:
                j += 1
                if i-j < 0 or i+j+1 > len(s)-1:
                    break
        if len(s) > 2 and i-k-1 >= 0 and i+k+1 <= len(s)-1:
            while s[i-k-1] == s[i+k+1]:
                k += 1
                if i-k-1 < 0 or i+k+1 > len(s)-1:
                    break
        output = max(output, 2*j, 2*k+1)
    print(output)
    return output


input = ['a', 'aa', 'baa', 'aab', 'abcdefghba', 'baablkj12345432133d']
result = list(map(longest_palindrome, input))
# %% 
'''
def longest_palondrome_2(s: str) -> int:
    output = 1
    for i in range(len(s)-1):
        j, k = 0, 0
        try:
            while s[i-j] == s[i+j+1]:
                j += 1
                if i-j < 0 or i+j+2 > len(s)-1:
                    break
        except:
            continue
        try:
            while s[i-k-1] == s[i+k+1]:
                # k += 1
                if i-k-1 < 0 or i+k+2 > len(s)-1:
                    break
                k += 1
        except:
            continue
        output = max(output, 2*j, 2*k+1)
    print(output)
    return output


input = ['a', 'aa', 'baa', 'aab', 'abcdefghba', 'baablkj12345432133d']
result = list(map(longest_palondrome_2, input))
'''