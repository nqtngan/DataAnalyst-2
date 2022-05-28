import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('D:\STUDY\BT DATA ANALYST\shopeep_koreantop_clothing_shop0_data.csv')
print(df.head())
print(df.info())

df = df.dropna()

#1 Vẽ biểu đồ so sánh số lượng shop gia nhập theo các năm.
plt.bar(df['join_year'], df['shopid'])
plt.title('Số lượng shop gia nhập theo các năm')
plt.xlabel('Năm')
plt.ylabel('Số lượng Shop')
plt.show()

#2 Vẽ biểu đồ thể hiện mối quan hệ giữa tỉ lệ phản hồi với số lượt khách hàng đánh giá tốt.
plt.scatter(df['response_rate'], df['rating_good'])
plt.title('Tỉ lệ phản hồi với số lượt khách hàng đánh giá tốt')
plt.xlabel('Tỉ lệ phản hồi')
plt.ylabel('số lượt khách hàng đánh giá tốt')
plt.show()

#3 Vẽ biểu đồ thể hiện mối quan hệ giữa thời gian phản hồi (đơn vị giây) với số lượt khách hàng đánh giá xấu.


#4 Vẽ biểu đồ thể hiện xu hướng của số lượng shop gia nhập theo thời gian.
plt.plot(df['join_year'], df['shopid'])
plt.title('Số lượng shop gia nhập theo các năm')
plt.xlabel('Năm')
plt.ylabel('Số lượng Shop')
plt.show()

#5 Vẽ biểu đồ thể hiện phân bố của điểm đánh giá trung bình. 
plt.hist(df['rating_star'], bins = 50)
plt.title('Sự phân bố của điểm đánh giá trung bình')
plt.show()
