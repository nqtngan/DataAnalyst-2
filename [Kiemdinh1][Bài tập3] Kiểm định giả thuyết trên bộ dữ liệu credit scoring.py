from cmath import nan
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from scipy import stats

df = pd.read_csv('D:\STUDY\BT DATA ANALYST\Credit_Scoring.csv')
df.dropna(inplace = True)
print(df.head())
print(df.info())

#Câu 1 Có phải những khách hàng không có người phụ thuộc sẽ có thu nhập trung bình theo tháng (MonthlyIncome) < những khách hàng có người phụ thuộc không (với mức ý nghĩa 10%)

sns.lmplot(x = 'NumberOfDependents', y = 'MonthlyIncome', data = df)
plt.show()

'''Dữ liệu cần xử lý'''
df1 = df.loc[:,['MonthlyIncome','NumberOfDependents']]
print(df1.head())

print('----------Dữ liệu KH có người phục thuộc----------')
df1_phuthuoc = df1[df1.NumberOfDependents >0]
print(df1_phuthuoc.head())
print(df1_phuthuoc.info())
print(df1_phuthuoc.describe())

print('----------Dữ liệu KH không người phục thuộc----------')
df1_khongPT = df1[df1.NumberOfDependents == 0]
print(df1_khongPT.head())
print(df1_khongPT.info())
print(df1_khongPT.describe())

'''Giả thuyết
H0 : a1 - a2 >= 0
H1 : a1 - a2 < 0
Với a1 : KH có người phụ thuộc
    a2 : KH không người phụ thuộc
Mức ý nghĩa 10%
'''

print(stats.ttest_ind(df1_phuthuoc.MonthlyIncome, df1_khongPT.MonthlyIncome, equal_var = False))
''' pvalue = 3.59295701688606e-90 < mức ý nghĩa 0.1
=> Bỏ H0, nhận H1
=> Không phải những khách hàng không có người phụ thuộc
sẽ có thu nhập trung bình theo tháng (MonthlyIncome) < những khách hàng có người phụ thuộc không (với mức ý nghĩa 10%)
'''

#Câu 2 Có phải trung bình số lượng khoản vay (NumberOfOpenCreditLinesAndLoans) những khách hàng gặp khó khăn trong vòng 2 năm trở lại đây (SeriousDlqin2yrs =1) thì sẽ cao hơn những khách hàng không gặp khó khăn không với mức ý nghĩa 10%

'''Dữ liệu cần xử lý'''
df2 = df.loc[:,['NumberOfOpenCreditLinesAndLoans','SeriousDlqin2yrs']]
print(df2.head())

print('---------- Dữ liệu KH khó khăn ----------')
df2_KK = df2[df2.SeriousDlqin2yrs == 1]
print(df2_KK.head())
print(df2_KK.info())
print(df2_KK.describe())

print('---------- Dữ liệu KH không khó khăn ----------')
df2_khongKK = df2[df2.SeriousDlqin2yrs == 0]
print(df2_khongKK.head())
print(df2_khongKK.info())
print(df2_khongKK.describe())

'''Giả thuyết
H0 : a1 - a2 >= 0
H1 : a1 - a2 < 0
Với a1 : KH khó khăn
    a2 : KH không khó khăn
Mức ý nghĩa 10%
'''

print(stats.ttest_ind(df2_KK.NumberOfOpenCreditLinesAndLoans, df2_khongKK.NumberOfOpenCreditLinesAndLoans, equal_var = False))
'''pvalue = 1.9377837295194415e-18 < mức ý nghĩa 0.01
=> Bỏ H0, chấp nhận H1
=> Không phải trung bình số lượng khoản vay của những khách hàng gặp khó khăn trong vòng 2 năm trở lại đây
sẽ cao hơn những khách hàng không gặp khó khăn không với mức ý nghĩa 10%'''
