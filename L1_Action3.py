# -*- coding: utf-8 -*-
'''
@author: RenQiang

Action3: 对汽车质量数据进行统计
数据集：car_complain.csv
600条汽车质量投诉
Step1，数据加载
Step2，数据预处理
拆分problem类型 = > 多个字段
Step3，数据统计
对数据进行探索：品牌投诉总数，车型投诉总数,哪个品牌的平均车型投诉最多
'''
import pandas as pd
# 导入汽车质量数据，并清洗数据（将品牌数据标准化）
car_complain = pd.read_csv('car_complain.csv')
car_complain['brand'].replace('一汽-大众','一汽大众',inplace=True)
# 将genres进行one-hot编码（离散特征有多少取值，就用多少维来表示这个特征）
result = car_complain.drop('problem', 1).join(car_complain.problem.str.get_dummies(','))

# 品牌投诉总数
result_brand = result.groupby(['brand'])['id'].agg(['count']).sort_values('count',ascending=False).reset_index()
print('品牌投诉总数为：')
print(result_brand.head())
print('其中品牌投诉总数最多的是：' + str(result_brand.iloc[0,0])+'品牌，投诉总数：'+ str(result_brand.iloc[0,1]))

# 车型投诉总数
result_car_model = result.groupby(['car_model'])['id'].agg(['count']).sort_values('count',ascending=False).reset_index()
print('车型投诉总数为：')
print(result_car_model.head())
print('其中车型投诉总数最多的是：' + str(result_car_model.iloc[0,0])+'车型，投诉总数：'+ str(result_car_model.iloc[0,1]))

# 按品牌和车型进行分类汇总，投诉数量计数
result_brand_model = result.groupby(['brand','car_model'])['id'].agg(['count'])

# 品牌的平均车型投诉排行。此问题描述有歧义，没有考虑到没有抱怨的车型，这样平均车型的结论有误导
result_brand_model_1 = result_brand_model.groupby(['brand'])['count'].agg(['mean']).sort_values('mean',ascending=False).reset_index()
print('品牌的平均车型投诉排行为：')
print(result_brand_model_1.head())
print('其中品牌的平均车型投诉最多的是：' + str(result_brand_model_1.iloc[0,0])+'品牌，投诉总数：'+ str(result_brand_model_1.iloc[0,1]))

# 单车型的投诉排行
result_brand_model_2 = result_brand_model.sort_values('count',ascending=False).reset_index()
print('单车型投诉排行为：')
print(result_brand_model_2.head())
print('其中单车型投诉最多的是：' + str(result_brand_model_2.iloc[0,1])+'车型，投诉总数：'+ str(result_brand_model_2.iloc[0,2]))
