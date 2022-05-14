from json import encoder
from turtle import color
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import OneHotEncoder, StandardScaler

df = pd.read_csv('D:\STUDY\BT DATA ANALYST\FoodPrice_in_Turkey.csv')
print(df.head())

#Vẽ biểu đồ CỘT so sánh giá gạo (Rice-Retail) tháng 12 năm 2019 của Ankara, Istanbul, Izmir và National Average.
data1 = df[(df['Year'] == 2019) & (df['Month'] == 12) & (df['ProductName'] == 'Rice - Retail')]
plt.bar(data1['Place'], data1['Price'])
plt.show()

#Vẽ biểu đồ ĐƯỜNG phân tích xu hướng giá gạo (Rice-Retail) trung bình cả nước (National Average) trong năm 2019 tại Thổ Nhĩ Kì.
data2 = df[(df['Year'] == 2019) & (df['ProductName'] == 'Rice - Retail') & (df['Place'] == 'National Average')]
plt.plot(data2['Month'], data2['Price'])
plt.title('Xu hướng giá gạo', fontsize  = 16, color = 'b')
plt.show()

# #Vẽ biểu đồ SCATTER phân tích mối liên quan giữa giá gạo và giá gas trung bình quốc gia (National Average) tại Thổ Nhĩ Kì.
x = df[(df['Place'] == 'National Average') & (df['ProductName'] == 'Fuel (gas) - Retail') & (df['Year'] == 2019)]
y = df[(df['Place'] == 'National Average') & (df['ProductName'] == 'Rice - Retail') & (df['Year'] == 2019)]
plt.scatter(x['Price'], y['Price'])
plt.title('Mối liên quan giữa giá gạo và giá gas', fontsize  = 16, color = 'b')
plt.show()