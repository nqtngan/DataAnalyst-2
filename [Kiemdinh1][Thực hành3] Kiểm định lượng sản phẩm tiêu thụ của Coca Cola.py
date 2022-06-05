import pandas as pd
from scipy import stats
import matplotlib.pyplot as plt

df = pd.read_excel('D:\STUDY\BT DATA ANALYST\Coca_cola_use.xlsx')
print(df.head())
print(df.info())
print(df.describe())

# Vẽ biểu đồ
df.boxplot()
plt.show()

'''Tiến hành kiểm định : Thực hiện kiểm định giả thuyết so sánh hai mẫu trung bình độc lập
Gọi a1, a2 lần lượt là lượng tiêu thụ coca trung bình trên đầu người ở Ohio và Atlanta
Giả thuyết H0 : a1-a2 =0
Giả thuyết H1 : a1-a2>0
mức ý nghĩa 5% . Loại kiểm định Independent T test'''

print (stats.ttest_ind(df.Ohio, df.Atlanta, equal_var = False))

'''Chúng ta nhìn thấy rằng: pvalue >5% rất nhiều nên không đủ cơ sở để bác bỏ giả thuyết không
Kết luận: Không đủ căn cứ để kết luận rằng lượng tiêu thụ coca trung bình ở Ohio > ở Atlanta'''