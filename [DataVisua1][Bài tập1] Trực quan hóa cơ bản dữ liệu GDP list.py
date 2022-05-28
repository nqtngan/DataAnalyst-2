from json import encoder
from turtle import color
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import OneHotEncoder, StandardScaler

df = pd.read_csv('D:\STUDY\BT DATA ANALYST\GDPlist.csv')
print(df.head())
print(df.info())

# #1.  So sánh GDP các nước ở South America.
# data1 = df[(df['Continent'] == 'South America') & (df['GDP (millions of US$)'])]
# print(data1.head())

# plt.bar(data1['Country'], data1['GDP (millions of US$)'])
# plt.title('So sánh GDP các nước ở South America', fontsize = 14)
# plt.xlabel('Country', fontsize = 12)
# plt.ylabel('millions of US$', fontsize = 12)
# plt.show()

#2 Đánh giá tỉ lệ đóng góp GDP của Việt Nam trên tổng số GDP của 5 nước Đông Nam Á là Vietnam,  Indonesia, Cambodia, Thailand và Malaysia.

#Chọn ra 5 nước theo y/c để làm so sánh
data2 = df[(df.Country == 'Vietnam') | (df.Country == 'Indonesia') | (df.Country == 'Cambodia') | (df.Country == 'Thailand') | (df.Country == 'Malaysia')]
print(data2.head())

plt.pie(data2['GDP (millions of US$)'], labels = data2['Country'], autopct='%1.2f%%')
plt.title('So sánh GDP 5 nước ở Châu Á', fontsize = 14)
plt.show()