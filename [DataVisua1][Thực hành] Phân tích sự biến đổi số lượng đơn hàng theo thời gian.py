from json import encoder
from turtle import color
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import OneHotEncoder, StandardScaler

df = pd.read_csv('D:\STUDY\BT DATA ANALYST\OnlineRetail.csv', encoding = 'ISO-8859-1')
print(df.head())
print(df.info)
print(df.info())
print(df.describe())

#Chọn mục tiêu Vẽ biểu đồ đường thể hiện xu hướng thay đổi số lượng đơn hàng theo thời gian trong năm 2011
#Vẽ biểu đồ cột so sánh số lượng đơn hàng trong các tháng của năm 2011.
df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'])
d1 = df[['InvoiceNo', 'InvoiceDate']]
d1 = d1.drop_duplicates(subset = 'InvoiceNo', keep = 'first')
d1 = d1.set_index(['InvoiceDate'])
d2 = d1['2011']
d2 = d2.reset_index()
d3 = d2.groupby(by=d2['InvoiceDate'].dt.date).count()

x = d3.index.get_level_values(0)
plt.bar(x, d3['InvoiceDate'])
plt.title('Số lượng đơn hàng thay đổi theo thời gian trong năm 2011', fontsize = 16)
plt.xlabel('Date', fontsize = 14)
plt.ylabel('#Invoices', fontsize = 14)
plt.show()