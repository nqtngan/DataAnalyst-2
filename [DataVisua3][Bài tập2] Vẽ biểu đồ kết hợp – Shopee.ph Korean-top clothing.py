import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime

df = pd.read_csv('D:\STUDY\BT DATA ANALYST\shopeep_koreantop_clothing_shop_data.csv')
print(df.head())
print(df.info())

df = df.dropna()

#1 Vẽ biểu đồ tần số số lượng shop gia nhập theo các năm.
sns.countplot(x = 'join_year', data = df)
plt.show()

#2 Vẽ biểu đồ xu hướng thể hiện mối quan hệ giữa tỉ lệ phản hồi với số lượt khách hàng đánh giá tốt.
sns.lmplot(x = 'response_rate', y = 'rating_good', data = df)
plt.show()

#**3 Vẽ biểu đồ xu hướng thể hiện mối quan hệ giữa thời gian phản hồi (đơn vị giây) với số lượt khách hàng đánh giá xấu.
new_df = df.loc[:, ['shopid', 'join_year', 'response_rate', 'rating_good', 'response_time', 'rating_bad',
                    'rating_star', 'is_shopee_verified', 'is_official_shop']]
new_df.head()

new_df.response_time = pd.to_datetime(new_df.response_time, format = '%H:%M:%S')
new_df['total_seconds'] = new_df.response_time.dt.second + new_df.response_time.dt.minute * 60 + new_df.response_time.dt.hour * 3600

sns.lmplot(x = 'total_seconds', y = 'rating_bad', data = new_df)
plt.show()


#4 Vẽ biểu đồ thể hiện phân bố của điểm đánh giá trung bình. 
sns.violinplot(x = 'rating_star', data = df)
plt.show()

#5 Vẽ biểu đồ tần số của cửa hàng chính thức và không chính thức. 
sns.countplot(x = 'is_official_shop', data = df)
plt.show()

#6 Vẽ biểu đồ tần số của cửa hàng được xác thực với chưa xác thực. 
sns.countplot(x = 'is_shopee_verified', data = df)
plt.show()
