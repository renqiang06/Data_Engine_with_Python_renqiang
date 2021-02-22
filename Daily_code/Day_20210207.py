#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@Time    :   2021/02/07 13:00:31
@Author  :   Ren Qiang 
@Contact :   renqiang06@126.com
'''
# Start
# 求1+3+...+99
print('1+3+...+99 = ', sum(range(1,100,2)))
print('1+3+...+99 = ' + str(sum(range(1,100,2))))

def DNA_strand_1(dna):
    for i in dna:
        i.replace(['A','T','C','G'],['T','A','G','C'])
    return dna