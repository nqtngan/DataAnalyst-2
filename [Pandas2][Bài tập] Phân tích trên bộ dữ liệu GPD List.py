from typing import ValuesView
import pandas as pd
import numpy as np

#1. Đọc bộ dữ liệu, cho biết số dòng, số cột và kiểu dữ liệu của các thuộc tính :
df = pd.read_csv('GDPlist.csv')
print(df.head())
# print(df.info())
# print(df.shape)
print('====================')

#2. Tính giá trị lớn nhất và nhỏ nhất của GDP:
df_GDP = df.loc[:,'GDP (millions of US$)']
print('Giá trị GDP nhỏ nhất : ', df_GDP.min())
print('Giá trị GDP lớn nhất : ', df_GDP.max())
print('====================')

#3. Hãy cho biết xu hướng phân bố dữ liệu của GDP.
print(df_GDP.mode())
print(df_GDP.median())
print(df_GDP.mean())
print(df.describe())
print('====================')

#4. Hãy cho biết châu lục nào xuất hiện nhiều nhất:
df_Continent = df.loc[:,'Continent']
print('Châu lục xuất hiện nhiều nhất : ', df_Continent.mode())
print('====================')

#5. Với mỗi châu lục hãy tính tổng GDP; trung bình cộng GDP. Hợp nhất 2 bảng này thành một bảng duy nhất gồm 3 thông tin: Tên châu lục; Tổng GDP; TBC GDP:
tongGDP = df.pivot_table (values = ['GDP (millions of US$)'], index = 'Continent', aggfunc = 'sum')
print('Tổng GDP : ', tongGDP)
print('------')

trungbinhGDP = df.pivot_table (values = ['GDP (millions of US$)'], index = 'Continent', aggfunc = 'mean')
print('Trung bình cộng GDP : ', trungbinhGDP)
print('------')

tonghop = pd.concat([tongGDP,trungbinhGDP], axis = 1)
print('Bảng hợp nhất:', tonghop)