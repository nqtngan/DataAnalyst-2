import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('D:\STUDY\BT DATA ANALYST\OnlineRetail.csv', encoding = 'ISO-8859-1')
print(df.head())
print(df.info())

df = df.dropna()

#Tính giá của mỗi mã sản phẩm ở các đơn hàng
df['Price'] = df['UnitPrice'] * df['Quantity']
print(df.head())
print(df.info())

#Biểu đồ phân bố cho giá sản phẩm
sns.violinplot(y = 'UnitPrice', data = df)
plt.show()

#Biểu đồ phân bố cho tổng giá mỗi sản phẩm ở các đơn
sns.violinplot(y = 'Price', data = df)
plt.show()

#Tính số lượng sản phẩm ở mỗi đơn hàng
soluong_df = df.groupby(['InvoiceNo'])['Quantity'].sum().reset_index()
print(soluong_df.head())

#Biểu đồ phân bố số lượng sản phẩm trên mỗi đơn
sns.violinplot(y = 'Quantity', data = soluong_df)
plt.show()

#Vẽ biểu đồ tần số số lượng sản phẩm mỗi quốc gia
slquocgia_df = df.groupby(['Country'])['Quantity'].sum().reset_index()
print(slquocgia_df.head())

df1 = df.drop_duplicates(subset = 'InvoiceNo')

sns.countplot(x = 'Country', data = df1)
plt.show()

#Biểu đồ box plot cho số lượng sản phẩm mỗi đơn
sns.boxplot(x = soluong_df['Quantity'])
plt.show()