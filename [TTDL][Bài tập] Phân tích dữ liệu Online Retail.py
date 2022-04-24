import pandas as pd
import numpy as np
import datetime as dt

print('1. Đọc bộ dữ liệu, cho biết số dòng, số cột và kiểu dữ liệu của các thuộc tính')
df = pd.read_csv('OnlineRetail.csv', encoding = 'ISO-8859-1')
print(df.head())
print(df.info())
print(df.shape)
print('=================\n')


print('2. Tạo cột mới có tên quý, "Previous" nhận giá trị 1 nếu ngày lập hóa đơn nằm trong các tháng 1,2,3; nhận giá trị 2 nếu ngày lập hóa đơn nằm trong các tháng 4,5,6; nhận giá trị 3 nếu ngày lập hóa đơn nằm trong các tháng 7,8,9; nhận giá trị 4 nếu ngày lập hóa đơn nằm trong các tháng 10,11,12')
df['month'] = pd.to_datetime(df['InvoiceDate'], format = '%m/%d/%Y %H:%M').dt.month

def quy(df):
    x = df['month']
    if 1 <= x <= 3 :
        return 1
    elif 4 <= x <= 6 :
        return 2
    elif 7 <= x <= 9 :
        return 3
    else:
        return 4
    
df['Previous'] = df.apply(quy, axis = 1)
# print(df.head())
truycap = df.loc[54000:162000,['Description','month','Previous']]
print(truycap)
print('=================\n')


print('3. Tạo một cột mới có tên "Amount" có giá trị bằng Quantity * UnitPrice')
df['Amount'] = df.Quantity * df.UnitPrice 
print(df.head())
print('=================\n')


print('4. Tạo cột mới "Discount" nhận giá trị 10% nếu Country là "United Kingdom" và thuộc quý 4, 5% nếu là "France" ngược lại là 0%')
df['month'] = pd.to_datetime(df['InvoiceDate'], format = '%m/%d/%Y %H:%M').dt.month

def giamgia(df):
    x = df['month']
    if df.Country == 'United Kingdom' and 10 <= x <= 12 :
        return 0.1
    elif df.Country == 'France' :
        return 0.05
    else :
        return 0
    
df['Discount'] = df.apply(giamgia, axis = 1)
# print(df.head())
truycap = df.loc[213:81000,['Country','month','Previous','Discount']]
print(truycap)
print('=================\n')


print('5. Tạo cột mới "Total" nhận giá trị bằng: Amount-Discount')
df['tien_Discount'] = df.Amount * df.Discount
df['Total'] = df.Amount - df.tien_Discount
print(df.head())