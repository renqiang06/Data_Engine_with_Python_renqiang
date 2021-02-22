#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# @Author  :   Ren Qiang
# %% 列表解析式 查找股票

stocks = {'MSFT': 165.51, 'FB': 174.79,
          'YHOO': 19.63, 'IBM': 121.15, 'GOOG': 1210.41}

stocks_150 = {v: k for k, v in stocks.items() if v > 150}
print(stocks_150)
