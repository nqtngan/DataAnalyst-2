import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('D:\STUDY\BT DATA ANALYST\GDPlist.csv')
print(df.head())
print(df.info())

df = df.dropna()

#----------BIỂU ĐỒ PHÂN BỐ----------
#Biểu đồ phân bố giá trị GDP toàn cầu
sns.violinplot(y = 'GDP (millions of US$)', data = df)
plt.show()

#Biểu đồ phân bố giá trị GDP châu Á
sns.violinplot(y = df[df['Continent'] == 'Asia']['GDP (millions of US$)'])
plt.show()

#Biểu đồ phân bố giá trị GDP châu Âu
sns.violinplot(y = df[df['Continent'] == 'Europe']['GDP (millions of US$)'])
plt.show()

#----------BIỂU ĐỒ BOXPLOT----------
#Biểu đồ box plot nhóm theo châu lục
sns.boxplot(x = 'Continent', y = 'GDP (millions of US$)' , data = df)
plt.show()
