from json import encoder
from turtle import color
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import OneHotEncoder, StandardScaler

df = pd.read_csv('D:\STUDY\BT DATA ANALYST\FoodPrice_in_Turkey.csv')
print(df.head())
print(df.info())

#1 Vẽ các biểu đồ cột so sánh giá Milk (powder, infant formula) và Fuel (gas) tháng 12 cuối năm năm 2019 của Ankara, Istanbul, Izmir và National Average.
dt1 = df[(df['Year'] == 2019) & (df['Month'] == 12) & (df['ProductName'] == 'Milk (powder, infant formula) - Retail')].reset_index()
dt2 = df[(df['Year'] == 2019) & (df['Month'] == 12) & (df['ProductName'] == 'Fuel (gas) - Retail')].reset_index()
data1 = pd.DataFrame({'x': dt1['Place'], 'Milk': dt1['Price'], 'Gas': dt2['Price']})

data1.plot(x = 'x', y = ['Milk', 'Gas'], kind = 'bar')
plt.title('Milk and Gas Price in 12/2019', fontsize = 12, color = 'b')
plt.xlabel('Place', fontsize = 11)
plt.ylabel('Price', fontsize = 11)
plt.show()


#2 Vẽ các biểu đồ đường phân tích xu hướng giá gạo (Rice-Retail), giá Fuel (gas) trung bình cả nước (National Average) trong năm 2016, 2018, 2019 tại Thổ Nhĩ Kì.
dt3 = df[(df['Year'] == 2016) & (df['ProductName'] == 'Rice - Retail') & (df['Place'] == 'National Average')].reset_index()
dt4 = df[(df['Year'] == 2016) & (df['ProductName'] == 'Fuel (gas) - Retail') & (df['Place'] == 'National Average')].reset_index()

dt5 = df[(df['Year'] == 2018) & (df['ProductName'] == 'Rice - Retail') & (df['Place'] == 'National Average')].reset_index()
dt6 = df[(df['Year'] == 2018) & (df['ProductName'] == 'Fuel (gas) - Retail') & (df['Place'] == 'National Average')].reset_index()

dt7 = df[(df['Year'] == 2019) & (df['ProductName'] == 'Rice - Retail') & (df['Place'] == 'National Average')].reset_index()
dt8 = df[(df['Year'] == 2019) & (df['ProductName'] == 'Fuel (gas) - Retail') & (df['Place'] == 'National Average')].reset_index()

fig, ax = plt.subplots(3, 2)

ax[0][0].plot(dt3['Month'], dt3['Price'], marker = '*', label = 'Rice-2016')
ax[0][0].plot(dt4['Month'], dt4['Price'], marker = 's', label = 'Gas-2016')
ax[0][0].set_ylabel('Price')
ax[0][0].set_xticklabels([])
ax[0][0].set_title('2016')

ax[1][0].plot(dt5['Month'], dt5['Price'], marker = '*', label = 'Rice-2018')
ax[1][0].plot(dt6['Month'], dt6['Price'], marker = 's', label = 'Gas-2018')
ax[1][0].set_ylabel('Price')
ax[1][0].set_xticklabels([])
ax[1][0].set_title('2018')

ax[2][0].plot(dt7['Month'], dt7['Price'], marker = '*', label = 'Rice-2019')
ax[2][0].plot(dt8['Month'], dt8['Price'], marker = 's', label = 'Gas-2019')
ax[2][0].set_ylabel('Price')
ax[2][0].set_xticklabels([])
ax[2][0].set_title('2019')

#============================

ax[0][1].scatter(dt3['Price'], dt4['Price'])
ax[0][1].set_title('2016')
ax[0][1].set_ylabel('Rice')
ax[0][1].set_xticklabels([])

ax[1][1].scatter(dt5['Price'], dt6['Price'])
ax[1][1].set_title('2018')
ax[1][1].set_ylabel('Rice')
ax[1][1].set_xticklabels([])

ax[2][1].scatter(dt7['Price'], dt8['Price'])
ax[2][1].set_title('2019')
ax[2][1].set_ylabel('Rice')
ax[2][1].set_xticklabels([])

plt.show()