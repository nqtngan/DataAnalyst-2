import pandas as pd
import numpy as np
import seaborn as sb
from sklearn.preprocessing import MinMaxScaler, RobustScaler, StandardScaler
from sklearn.preprocessing import LabelEncoder, OneHotEncoder, OrdinalEncoder
import matplotlib.pyplot as plt

df = pd.read_csv('D:\STUDY\BT DATA ANALYST\FoodPrice_in_Turkey.csv', encoding = 'ISO-8859-1')
print(df.head())
print(df.describe())
print(df.info())

# kiểm tra dữ liệu bị khuyết
print(df.isna())

#Xử lý dữ liệu ngoại lai cho đặc trưng PriceIn [ ]:
sb.boxplot(x=df['Price'])  # vẽ box plot cho dữ liệu ở cột Price
print(plt.show)