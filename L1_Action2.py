# -*- coding: utf-8 -*-
'''
@author: RenQiang

Action2: 统计全班的成绩
班里有5名同学，现在需要你用Python来统计下这些人在
语文、英语、数学中的
平均成绩、最小成绩、最大成绩、方差、标准差。
然后把这些人的总成绩排序，得出名次进行成绩输出（可以用numpy或pandas）
姓名    语文    数学    英语
张飞    68      65      30  
关羽    95      76      98
刘备    98      86      88
典韦    90      88      77
许褚    80      90      90
'''
import pandas as pd
data = {'语文': [68, 95, 98, 90, 80], '数学': [65, 76, 86, 88, 90],
        '英语': [30, 98, 88, 77, 90]}
df = pd.DataFrame(data, index=['张飞', '关羽', '刘备', '典韦', '许褚'])
# b = df.reset_index() # 姓名不作为索引
# c = df.reset_index(drop=True) # 把姓名抹掉，保留成绩

print(df.describe())  # 只有count, mean, std, min, max 。没有var，需要单独列出
print('平均成绩为：')
print(df.mean())
print('最小成绩为：')
print(df.min())
print('最大成绩为：')
print(df.max())
print('成绩方差为：')
print(df.var())
print('成绩标准差为：')
print(df.std())

# 对各位成员按成绩进行求和
get_sum = df.apply(lambda x: x.sum(), axis=1).sort_values(ascending=False)
rank = get_sum.rank(ascending=False).astype(int)
print('总成绩排序：')
print(get_sum)
print('名次为：')
print(rank)
