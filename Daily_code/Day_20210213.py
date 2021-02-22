#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# @Author  :   Ren Qiang
# %% 打擂法，确定买卖股票的最佳时机，假设T+0,不可做空，买卖一次
def maxProfit(prices: list) -> int:
    buy, sell, maxProfit = [1], [1], 0
    try:
        for i in range(len(prices)):
            for j in range(i, len(prices)):
                Profit = prices[j] - prices[i] # 收益
                if Profit > maxProfit:
                    buy[0], sell[0], maxProfit = i+1, j+1, Profit
                elif Profit == maxProfit and Profit: # 有相同最大收益，择优
                    if i+1 in buy: # 同一天买，则卖的早好
                        continue
                    elif j+1 in sell: # 同一天卖，则买的晚好
                        buy[sell.index(j+1)] = i+1
                    else:
                        buy.append(i+1), sell.append(j+1) #其他解
        print(prices, '\t第{}天买,第{}天卖,做多可收益{}'.format(buy, sell, maxProfit))
        return buy, sell, maxProfit
    except Exception as r:
        print('错误 %s' % r)


input = [[7, 1, 5, 3, 6, 4], [7, 6, 4, 3, 1], [5, 10, 1, 5, 5], [2, 2, 12, 1, 1, 11]]
result = list(map(maxProfit, input))
# %% 买卖股票的最佳时机，假设T+0,不可做空，买卖一次
def maxProfit_2(prices: list) -> int:
    maxProfit =  0
    P_buy = prices[0]
    for i in range(len(prices)):
        Profit = prices[i] - P_buy
        maxProfit = max(maxProfit, Profit)
        P_buy = min(P_buy, prices[i])
        
    # print(maxProfit)
    return maxProfit

input = [[7, 1, 5, 3, 6, 4], [7, 6, 4, 3, 1], [5, 10, 1, 5, 5], [2, 2, 12, 1, 1, 11]]
result = list(map(maxProfit_2, input))
# %% 买卖股票的最佳时机，假设T+0,买入后能立即卖出
'''

def maxProfit_err(prices: list) -> int:
    try:
        T_buy = 0
        for i in range(len(prices)):
            if prices[i] <= prices[T_buy]:  # 先找出理论最低买点,越晚越好
                T_buy = i
        T_sell = T_buy
        for j in range(T_buy, len(prices)):
            if prices[j] > prices[T_sell]:  # 从最低买点检索最高卖点，越早越好
                T_sell = j
        output = prices[T_sell]-prices[T_buy]  # 理论最大利润
        print(prices, '\t第{}天买,第{}天卖,收益{}'.format(T_buy+1, T_sell+1, output))
        return output
    except Exception as r:
        print('错误 %s' % r)


input = [[7, 1, 5, 3, 6, 4], [7, 6, 4, 3, 1], [1, 3, 2, 1, 4, 2, 4]]
result = list(map(maxProfit_err, input))
'''
