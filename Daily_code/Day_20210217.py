#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# @Author  :   Ren Qiang
# %% 宝石还是石头
import re


def numJewelsInStones(J: str, S: str) -> int:
    S = re.subn('[{}]'.format(J), '', S)
    output = S[1]
    print(output)
    return output


numJewelsInStones('aA', 'aAAbbbb')
numJewelsInStones('z', 'ZZ')

# %%


