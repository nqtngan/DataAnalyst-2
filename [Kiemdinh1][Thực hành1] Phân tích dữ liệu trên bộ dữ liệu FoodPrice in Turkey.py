import pandas as pd
from scipy import stats
import matplotlib.pyplot as plt

df = pd.read_csv('D:\STUDY\BT DATA ANALYST\FoodPrice_in_Turkey.csv')
print(df.head())
print(df.info())

#1 Với mức ý nghĩa 5% hay kiểm định giả thuyết:
#giá bán lẻ gạo trung bình năm 2019 là 9.5 (Lira)/1 kg Turkish Lira là đơn vị tiền tệ ở Turkey (1usd ~ 8-9 Lira)

#liệt kê tên các sản phẩm
product_names = list(df['ProductName'].unique()) 
print(product_names)

# Lọc bản ghi liên quan tới giá gạo năm 2019
df_rice1 = df.loc[(df.ProductName == 'Rice - Retail') & (df.Year == 2019)]
print ('Số lượng bản ghi gạo năm 2019: ', str(df_rice1.shape[0])) 

#Vẽ biểu đồ
df_rice1.Price.hist()
plt.show()

#H0 : Giá gạo tb = 9.5
#H1 : Giá gạo tb # 9.5

print(stats.ttest_1samp(df_rice1.Price, 9.5))

# Lọc bản ghi liên quan tới giá gạo năm 2020 (câu hỏi thêm)
df_rice2 = df.loc[(df.ProductName == 'Rice - Retail') & (df.Year == 2018)]
print ('Số lượng bản ghi gạo năm 2018: ', str(df_rice2.shape[0]))
print(stats.ttest_ind(df_rice1.Price, df_rice2.Price))