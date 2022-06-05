from cmath import nan
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from scipy import stats

df = pd.read_csv('D:\STUDY\BT DATA ANALYST\house_price_Dống-Da_Hà-Nội_subdata.csv')
print(df.head())
print(df.info())
print(df.describe())

#1. Vẽ biểu đồ so sánh phân phối giá (triệu đ/m2) giữa nhà Phố và Nhà ngõ
df['dongia'] = df.price / df.area
sns.kdeplot(x = 'dongia', hue = 'property_type', data = df)
plt.show()

#==============================
#2. Kiểm định giả thuyết giá (triệu đ/m2) nhà mặt phố > giá nhà trong ngõ, với mức ý nghĩa 5%
'''Giả thuyết:
H0 : giá nhà phố > giá nhà ngõ
H1 : giá nhà phố < giá nhà ngõ
Mức ý nghĩa 5%
'''

#Lấy giá trị nhà theo khu vực :
df_nhapho = df[df.property_type == 'mat pho']
df_nhango = df[df.property_type == 'trong ngo']

print(stats.ttest_ind(df_nhapho.dongia , df_nhango.dongia, equal_var = False))
'''pvalue = nan --> không có giá trị để kiểm định được giả thuyết'''

#==============================
#3. Giá của những căn nhà không có thông tin về giấy tờ pháp lý thấp hơn giá nhà những căn có thông tin về giấy tờ pháp lý với mức ý nghĩa 5%
'''Giả thuyết:
H0 : giá nhà không có giấy tờ PL < giá nhà có giấy tờ PL
H1 : giá nhà không có giấy tờ PL > giá nhà có giấy tờ PL
Mức ý nghĩa 5%
'''

#Lấy giá trị nhà theo nhà có giấy tờ hay không có giấy tờ :
df_coPL = df[df.land_certificate == 'So do']
df_khongPL = df[df.land_certificate == '']

print(stats.ttest_ind(df_coPL.price, df_khongPL.price, equal_var = False))
