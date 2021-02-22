#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# @Author  :   Ren Qiang
# %% 股票统计 前提：字典key不能重复
from heapq import nlargest as nl


name = ['MSFT', 'FB', 'YHOO', 'IBM', 'GOOG']
shares = [150, 50, 320, 100, 75]
price = [165.51, 174.79, 19.63, 121.15, 1210.41]

dic_price = dict(zip(price, name))
top2_price = [dic_price[i] for i in nl(2, dic_price)]

dic_shares = dict(zip(shares, name))
top2_shares = [dic_shares[i] for i in nl(2, dic_shares)]

print('股票价格最高的两只股票：', top2_price)
print('买入股数最高的两只股票：', top2_shares)

# %% 股票统计
'''
from heapq import nlargest as nl


name = ['MSFT', 'FB', 'YHOO', 'IBM', 'GOOG']
shares = [150, 50, 320, 100, 75]
price = [165.51, 174.79, 19.63, 121.15, 1210.41]
dic1 = dict(zip(price, name))
dic2 = dict(zip(shares, name))

max_price = list(map(lambda x: dic1[x], nl(2, dic1)))
print(max_price)
max_shares = list(map(lambda x: dic2[x], nl(2, dic2)))
print(max_shares)
'''
# %%
'''
def heapq_shares2(data):
    max_price = nl(2, data, key = lambda x:x['price'])
    max_shares = nl(2, data, key = lambda x:x['shares'])
    pprint(max_price, indent=2)
    pprint(max_shares, indent=2)
    return max_price, max_shares
shares = [
    {'name': 'MSFT', 'shares': 150, 'price': 165.51},
    {'name': 'FB', 'shares': 50, 'price': 174.79},
    {'name': 'YHOO', 'shares': 320, 'price': 19.63},
    {'name': 'IBM', 'shares': 100, 'price': 121.15},
    {'name': 'GOOG', 'shares': 75, 'price': 1210.41}
]
heapq_shares2(shares)
'''
