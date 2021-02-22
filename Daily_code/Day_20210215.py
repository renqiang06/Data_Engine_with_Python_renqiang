#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# @Author  :   Ren Qiang
# %% 排列组合 输入一个字符串，返回所有可能的排列，并去重
def permutations(string):
    output = []
    if len(string) > 1:
        for i in range(len(string)):
            for j in permutations(string[0:i]+string[i+1:]):  # 剔除第i个数
                output.append(string[i]+j)
    else:
        output = string    # 返回本身
    output = list(set(output))
    return output

input = ['a', 'ab', 'aabb']
result = list(map(permutations, input))
print(result)

# %%
'''
def permutations00(string):
    L_s = list(string)
    s = set(L_s)
    output = []
    for i in s:
        L_s.remove(i)
        string = ''.join(L_s)
        for j in permutations00(string):
            output.append(i+j)
    print(output)
    return output


input = ['aabb']
# output = []
result = list(map(permutations00, input))
'''

# %%
'''
def permutation(str):
    nums, output = list(str), []
    
    def permut(nums, start=0):
        if start == len(nums) - 1:
            output.append(''.join(nums))
            return output
        dup = set()
        for i in range(start, len(nums)):
            if nums[i] in dup:
                continue
            dup.add(nums[i])
            nums[i], nums[start] = nums[start], nums[i]
            permut(nums, start + 1)
            nums[i], nums[start] = nums[start], nums[i]
    permut(nums, start=0)
    return output


input = ['a', 'ab', 'aabb']
result = list(map(permutations_1, input))
print(result)
'''
