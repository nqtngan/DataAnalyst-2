import pandas as pd
import numpy as np
import seaborn as sb
from sklearn.preprocessing import MinMaxScaler, RobustScaler, StandardScaler
from sklearn.preprocessing import LabelEncoder, OneHotEncoder, OrdinalEncoder
import matplotlib.pyplot as plt

df = pd.read_csv('D:\STUDY\BT DATA ANALYST\OnlineRetail.csv', encoding = 'ISO-8859-1')
print(df.head())
print(df.info())

# kiểm tra dữ liệu bị khuyết
print(df.isna())

# kiểm tra dữ liệu không bị khuyết
print(df['CustomerID'].notna())

# in những dòng ngoại lai Quantity < 0
print(df[df['Quantity'] < 0])

#Xử lý dữ liệu ngoại lai
sb.boxplot(x=df['Quantity'])  # vẽ box plot cho dữ liệu ở cột Quantity
print(plt.show())

