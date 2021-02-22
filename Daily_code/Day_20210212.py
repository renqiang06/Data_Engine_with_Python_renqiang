#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# @Author  :   Ren Qiang
# %% 队列中的移动平均值
import queue as q


class MovingAverage:
    def __init__(self, size: int):
        self.Q = q.Queue(size)

    def next(self, val: int) -> float:
        if self.Q.full():
            self.Q.get()
        self.Q.put(val)
        output = sum(self.Q.queue)/self.Q.qsize()
        print(output)
        return output


input = [1, 10, 5, 6]
size = 3
m = MovingAverage(size)
result = list(map(m.next, input))
# %%
'''
class MovingAverage2:
    def __init__(self, size: int):
        self.Q = q.Queue(size)

    def next(self, val: int) -> float:
        if self.Q.full():
            self.Q.get()
        self.Q.put(val)
        output = sum(self.Q.queue)/self.Q.qsize()
        print(output)
        return output


input = [1, 10, 5, 6]
num = 3
m = MovingAverage2(num)
result = list(map(m.next, input))

'''
