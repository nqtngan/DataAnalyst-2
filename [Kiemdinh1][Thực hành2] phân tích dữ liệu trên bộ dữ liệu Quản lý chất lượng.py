import pandas as pd
from scipy import stats
import matplotlib.pyplot as plt

df = pd.read_excel('D:\STUDY\BT DATA ANALYST\Quality.xlsx')
print(df.head())
print(df.info())

#Với mức ý nghĩa 0.01 tiến hành kiểm định chất lượng sản phẩm

# Tiền xử lý dữ liệu - gom hết dữ liệu của 4 mẫu thành 1 mảng duy nhất
sample = list()
for i in df.columns:
    sample.extend(df[i].tolist())

# tiến hành mô tả dữ liệu mẫu
df = pd.DataFrame(columns=['sample'], data= sample) 
print(df.head())
print(df.describe())

'''Dựa vào kết quả phân tích trên: bộ dữ liệu chứa đủ 120 mẫu
Giá trị trung bình trên mẫu đúng bằng 12, giống mô tả của khách hàng
Phương sai: = 0.223108 (sai số so với giá trị trung bình của mẫu dữ liệu) >0.21 ==> khách hàng nên thay đổi lại tuyên bố về sai số của mình
Tiến hành kiểm định về giá trị trung bình
Giả thuyết H0 : khối lượng trung bình của sản phẩm = 12
Giả thuyết H1 : Khối lượng trung bình của sản phẩm # 12
Thực hiện phép kiểm định: One Sample T Test'''

print (stats.ttest_1samp(sample,12))
'pvalue = 0.6042828222996104 > 0.01 ==> chấp nhận H0'
