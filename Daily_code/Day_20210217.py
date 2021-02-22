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


# https://prod.liveshare.vsengsaas.visualstudio.com/join?A54E79F2B23BB8A10896DDDA2DA92C92FC74
# f3389f98-f98b-42c3-b8de-5d72b470220a