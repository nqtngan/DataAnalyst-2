import pandas as pd
import numpy as np

#1. Đọc bộ dữ liệu, cho biết số dòng, số cột và kiểu dữ liệu của các thuộc tính.
print('1/ Đọc bộ dữ liệu, cho biết số dòng, số cột và kiểu dữ liệu của các thuộc tính')
df = pd.read_csv('OnlineRetail.csv', encoding = 'ISO-8859-1')
print(df.head())
print(df.tail())
print(df.info())
print('==================\n')


#2. Xây dựng bảng Pivot table, với mỗi Số hóa đơn tính trung bình cộng số lượng các mặt hàng theo từng Quốc gia. 
print('2/ Xây dựng bảng Pivot table, với mỗi Số hóa đơn tính trung bình cộng số lượng các mặt hàng theo từng Quốc gia')
tbc_slhang = df.pivot_table(values = 'Quantity', index = ['Country','InvoiceNo','Description'], aggfunc = 'mean')
print(tbc_slhang)
print('==================\n')


#3. Xây dựng bảng Pivot table, với mỗi Khách hàng cho biết số lượng mua hàng lớn nhất và nhỏ nhất theo Kho.
print('3/ Xây dựng bảng Pivot table, với mỗi Khách hàng cho biết số lượng mua hàng lớn nhất và nhỏ nhất theo Kho')
slhang_max = df.pivot_table(values = 'Quantity', index = ['StockCode','CustomerID'], aggfunc = 'max')
print('SL hàng max:', slhang_max)
print('--------')

slhang_min = df.pivot_table(values = 'Quantity', index = ['StockCode','CustomerID'], aggfunc = 'min')
print('SL hàng min:', slhang_min)
print('--------')

tonghop1 = pd.concat([slhang_max,slhang_min],axis = 1)
print(tonghop1)
print('==================\n')


#4. Xây dựng bảng Pivot table, với mỗi Mã kho tính tổng số lượng các mặt hàng và trung bình cộng giá.
print('4/ Xây dựng bảng Pivot table, với mỗi Mã kho tính tổng số lượng các mặt hàng và trung bình cộng giá')
tonghang = df.pivot_table(values = 'Quantity', index = ['StockCode','Description'], aggfunc = 'sum')
print('Tổng hàng:', slhang_max)
print('--------')

tbcgia = df.pivot_table(values = 'UnitPrice', index = ['StockCode','Description'], aggfunc = 'mean')
print('TB giá:', tbcgia)
print('--------')

tonghop2 = pd.concat([tonghang, tbcgia], axis = 1)
print(tonghop2)
print('==================\n')


#5. Xây dựng bảng Pivot table cho biết tổng số lượng hàng bán được của mỗi ngày.
print('5/ Xây dựng bảng Pivot table cho biết tổng số lượng hàng bán được của mỗi ngày')
tonghang_moingay = df.pivot_table(values = 'Quantity', index = 'InvoiceDate', aggfunc = 'sum')
print(tonghang_moingay)