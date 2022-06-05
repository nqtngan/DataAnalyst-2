import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from scipy import stats

df = pd.read_csv('D:\STUDY\BT DATA ANALYST\GDPlist.csv')
print(df.head())
print(df.info())
print(df.describe())

df.rename(columns = {'GDP (millions of US$)':'GDP'}, inplace = True)  

#1. Kiểm định Trung bình GDP của các quốc gia trên thế giới là 500 tỉ usd/năm
#Vẽ biểu đồ
sns.histplot(df.GDP)
plt.show()

# '''Giả thuyết
# H0 = 500 tỷ USD/năm
# H1 # 500 tỷ USD/năm
# Mức ý nghĩa 1%
# '''
# print(stats.ttest_1samp(df.GDP, 500000))

# '''Do pvalue=0.7077493494055246 > 1% ==> không đủ căn cứ bác bỏ H0
# ==> Giá trị Trung bình GDP của các quốc gia trên thế giới là 500 tỉ usd/năm'''

# #=======================
# #2. GDP trung bình ở các quốc gia ở châu Âu cao hơn châu Á không
# '''Giả thuyết
# H0 : GDP Châu Âu > Châu Á
# H1 : GDP Châu Âu # Châu Á
# Mức ý nghĩa 1%
# '''

# print('Xét số liệu ở Châu Âu:')
# df_ChauAu = df[df.Continent == 'Europe']
# df_ChauAu.sort_values(by = 'GDP', ignore_index = True, inplace = True)
# print(df_ChauAu)

# print('Xét số liệu ở Châu Á:')
# df_ChauA = df[df.Continent == 'Asia']
# df_ChauA.sort_values(by = 'GDP', ignore_index = True, inplace = True)
# print(df_ChauA)

# print('So sánh số liệu giữa Châu Âu và Châu Á:')
# d = df_ChauAu.GDP - df_ChauA.GDP
# print(stats.wilcoxon(d, alternative = 'greater'))

# '''pvalue = 0.9992904785457841 > 0.01 (1%)
# --> Chấp nhận H0 , bác bỏ H1
# --> GDP trung bình ở các quốc gia ở châu Âu > châu Á'''

#=======================
#3. GDP trung bình của các quốc gia ở châu Âu và châu Mỹ là bằng nhau
'''Giả thuyết
H0 : GDP Châu Âu = Châu Mỹ
H1 : GDP Châu Âu # Châu Mỹ
Mức ý nghĩa 1%
'''

print('Xét số liệu ở Châu Âu:')
df_ChauAu = df[df.Continent == 'Europe']
df_ChauAu.sort_values(by = 'GDP', ignore_index = True, inplace = True)
print(df_ChauAu)

print('Xét số liệu ở Châu Mỹ:')
df_ChauMy = df[(df.Continent == 'South America') | (df.Continent == 'North America')]
df_ChauMy.sort_values(by = 'GDP', ignore_index = True, inplace = True)
print(df_ChauMy)

print('So sánh số liệu giữa Châu Âu và Châu Mỹ:')
d = df_ChauAu.GDP - df_ChauMy.GDP
print(stats.wilcoxon(d, alternative = 'two-sided'))

'''pvalue = 0.0000001 < 0.01
--> Bác bỏ H0, chấp nhận H1
--> GDP trung bình của các quốc gia ở châu Âu và châu Mỹ là khác nhau
'''