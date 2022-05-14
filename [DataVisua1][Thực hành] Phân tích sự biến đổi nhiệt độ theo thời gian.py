from json import encoder
from turtle import color
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import OneHotEncoder, StandardScaler

df = pd.read_csv('D:\STUDY\BT DATA ANALYST\daily-min-temperatures.csv')
print(df.head())
print(df.info)

#Chọn mục tiêu Vẽ biểu đồ Histogram phân tích các giá trị thống kê như max, min, mode, tần suất.
#Vẽ biểu đồ đường phân tích xu hướng thay đổi nhiệt độ theo thời gian.
print(df['Temp'].describe())
plt.hist(df['Temp'], bins = 45)
plt.title('Xu hướng thay đổi nhiệt độ theo thời gian', fontsize = 12, color = 'b')
plt.show()