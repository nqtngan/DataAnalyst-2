import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('D:\STUDY\BT DATA ANALYST\FoodPrice_in_Turkey.csv')
print(df.head())
print(df.info())

df = df.dropna()

#VẼ BIỂU ĐỒ

#Lọc dữ liệu sản phẩm gạo, vẽ biểu đồ xu hướng qua các năm
rice_df = df[df['ProductId'] == 52]
sns.lmplot(x = 'Year', y = 'Price' , data = rice_df)
plt.show()

#Biểu đồ phân bố cho giá sản phẩm
sns.violinplot(y = 'Price', data = df)
plt.show()

#vẽ biểu đồ tần số cho các sản phẩm theo năm
sns.countplot(x = 'Year', data = df)
plt.show()


#Thống kê sản phẩm theo địa điểm
sns.countplot(x = 'Place', data = df)
plt.show()
