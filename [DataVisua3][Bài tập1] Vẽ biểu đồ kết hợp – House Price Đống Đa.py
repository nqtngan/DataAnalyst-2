import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_excel('D:\STUDY\BT DATA ANALYST\house_price_dongda.xlsx')
print(df.head())
print(df.info())

df = df.dropna()

#1/ Vẽ biểu đồ xu hướng phân tích mối quan hệ giữa giá nhà với diện tích, giá nhà với số lượng phòng ngủ, nhận xét.

sns.lmplot(x = 'area', y = 'price', data = df)
sns.lmplot(x = 'bedroom', y = 'price', data = df)
plt.show()

#2/ Vẽ biểu đồ phân bố thể hiện phân bố của giá nhà theo các hướng, nhận xét.
sns.violinplot(x = 'house_direction', y = 'price', data = df)
plt.show()

#3/ Vẽ biểu đồ tần số để đếm số nhà ở mỗi hướng nhà, nhận xét.
sns.countplot(x = 'house_direction', data = df)
plt.show()

#4/ Vẽ biểu đồ boxplot thể hiện phân bố của giá nhà theo các hướng, nhận xét.
sns.boxplot(x = 'house_direction', y = 'price', data = df)
plt.show()
