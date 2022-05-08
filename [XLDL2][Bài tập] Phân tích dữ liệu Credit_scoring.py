import pandas as pd
import numpy as np
import seaborn as sns
from sklearn.preprocessing import MinMaxScaler, RobustScaler, StandardScaler
from sklearn.preprocessing import LabelEncoder, OneHotEncoder, OrdinalEncoder
import matplotlib.pyplot as plt
from sympy import principal_branch

df = pd.read_csv('D:\STUDY\BT DATA ANALYST\Credit_Scoring.csv')

#Nêu thông tin về kiểu dữ liệu và khoảng dữ liệu ở các cột
print(df.head())
print(df.info())

# Thay thế giá trị khuyết thiếu bằng giá trị nội suy theo các cột
df1 = df.interpolate(method = 'linear', axis = 0).ffill().bfill()
print(df1.head())
print(df1.info())

#Kiểm tra dữ liệu khuyết thiếu và thay bằng 0
df2 = df.fillna(0)
print(df2.info())
print(df2.isna())

# #Vẽ biểu đồ boxplot, biểu đồ phân bố dữ liệu cho các cột
# #Biểu đồ boxplot cột MonthlyIncome
# sns.boxplot (x = df1.MonthlyIncome)
# print(plt.show())

# #Biểu đồ phân bố dữ liệu kdeplot cột MonthlyIncome
# sns.kdeplot (x = df1.MonthlyIncome)
# print(plt.show())

# #Biểu đồ boxplot cột DebtRatio
# sns.boxplot (x = df1.DebtRatio)
# print(plt.show())

# #Biểu đồ phân bố dữ liệu kdeplot cột DebtRatio
# sns.kdeplot (x = df1.DebtRatio)
# print(plt.show())

# #Loại bỏ giá trị ngoại lai
# Q1 = df1.MonthlyIncome.quantile(0.25)
# Q3 = df1.MonthlyIncome.quantile(0.75)
# IQR = Q3 - Q1
# print(IQR)

#Chia dữ liệu ở các cột Age và MonthlyIncome thành 5 nhóm theo các khoảng: 0, 30, 40, 50, 80, 150 và đếm số lượng phần tử ở mỗi nhóm.
#Cột Age
print(df1.age.unique())
bins = [0, 30, 40, 50, 80, 150]
ten_nhomtuoi = ['U30', 'U40', 'U50', 'U80', 'Old']
age_range = pd.cut(df1.age, bins, labels = ten_nhomtuoi)
print(age_range)
