import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_excel('D:\STUDY\BT DATA ANALYST\house_price_dongda.xlsx')
print(df.head())
print(df.info())

df = df.dropna()

#1 Vẽ biểu đồ phân tích
#Lấy các cột cần phân tích
data1 = df.loc[:,['area','bedroom','toilet','price']]
print(data1.head())

#mối liên hệ giữa diện tích với giá nhà
plt.scatter(data1['area'], data1['price'])
plt.title('Mối liên hệ giữa diện tích với giá nhà')
plt.xlabel('Diện tích (m2)')
plt.ylabel('Giá nhà (Triệu VND)')
plt.show()

#mối liên hệ giữa số phòng ngủ với giá nhà
plt.scatter(data1['bedroom'], data1['price'])
plt.title('Mối liên hệ số phòng ngủ với giá nhà')
plt.xlabel('Số phòng ngủ')
plt.ylabel('Giá nhà (Triệu VND)')
plt.show()

#mối liên hệ giữa số toilet với giá nhà
plt.scatter(data1['toilet'], data1['price'])
plt.title('Mối liên hệ số toilet với giá nhà')
plt.xlabel('Số toilet')
plt.ylabel('Giá nhà (Triệu VND)')
plt.show()