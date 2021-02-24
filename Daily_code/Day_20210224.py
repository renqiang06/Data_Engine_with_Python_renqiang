#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = 'Ren Qiang'
# %% 最小时间差 hash
from datetime import datetime as dt


def findMinDifference(timePoints: list) -> int:
    output = 1439
    time_set = {int(i[:2])*60+int(i[3:]) for i in timePoints}
    if len(time_set) != len(timePoints):
        return 0
    time_list = list(time_set)
    time_list.sort()
    time_list.append(time_list[0]+1440)
    for i in range(len(time_list)-1):
        diff = time_list[i+1] - time_list[i]
        output = min(diff, output)
    print(output)
    return output


if __name__ == '__main__':
    input = [['23:59', '00:00'],
             ['21:59', '00:30', '00:05', '20:55'],
             ['23:59', '00:30', '00:05', '20:55']]
    result = list(map(findMinDifference, input))
# %% 最小时间差 no hash


def findMinDifference2(timePoints: list) -> int:
    output = 1439
    for i in range(len(timePoints)-1):
        for j in range(i+1, len(timePoints)):
            T1 = dt.strptime(timePoints[i], '%H:%M')
            T2 = dt.strptime(timePoints[j], '%H:%M')
            diff = int((T2-T1).seconds/60)
            output = min(1440-diff, diff, output)
    print(output)
    return output


if __name__ == '__main__':
    input = [['23:59', '00:00'],
             ['21:59', '00:30', '00:05', '20:55'],
             ['23:59', '00:30', '00:05', '20:55']]
    result = list(map(findMinDifference2, input))
