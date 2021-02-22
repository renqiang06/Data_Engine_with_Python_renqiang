#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# @Author  :   Ren Qiang
# ACtion2 互补DNA 其中，A与T互补，C与G互补编写函数DNA_strand(dna)
# %% 自己的做法

def DNA_strand(dna):
    out = ''
    for i in dna:
        # print(i)
        if i == 'A':
            out += 'T'
        elif i == 'T':
            out += 'A'
        elif i == 'C':
            out += 'G'
        elif i == 'G':
            out += 'C'
        else:
            print("输入的数据中有非ATCG字符，异常字符为：", i)
    print(dna + ' 转录后为：' + out)
    return out


DNA_strand("ATTGC")
DNA_strand("AAAA")
DNA_strand("ATCGT")
# %% 借鉴优秀案例1

Dict = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
DNA_input = ['ATTGC', 'AAAA', 'ATCGT']


def DNA_trans_1(dna):
    out = ''
    for i in dna:
        try:
            out += Dict[i]
        except:
            out += '{' + i + '}'
            print(dna + '\t中有非ATCG字符：' + i)
    print(dna + '\t转录后为：' + out)
    return out


print('优秀案例1:')
result = list(map(DNA_trans_1, DNA_input))
# %% 借鉴优秀案例2


def DNA_trans_2(dna):  # 定义转录函数
    key = 'GACT'  # 构建巧妙的索引循环
    output = ''
    for i in dna:
        try:
            output += key[key.index(i.upper())-2]
        except:
            output += '{' + i + '}'  # 标注非标准字符
            print(dna, '\t中有非ATCG字符：', i)
    print(dna, '\t转录后为：', output)
    return output


DNA_input = ['qttgc', 'AAAA', 'ATCGT']  # 输入
print('优秀案例2:')
result = list(map(DNA_trans_2, DNA_input))  # 调用转录函数

# %%
