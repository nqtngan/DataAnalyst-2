import pandas as pd

#1. Đọc bộ dữ liệu, cho biết số dòng, số cột và kiểu dữ liệu của các thuộc tính.
print('1. Đọc bộ dữ liệu, cho biết số dòng, số cột và kiểu dữ liệu của các thuộc tính')
df = pd.read_excel('house_price_dongda1.xlsx')
print(df.head(16))
print(df.info())
print('==============\n')


#2. Lọc ra các bản ghi bán nhà riêng tại phường Trung liệt hoặc phường Khâm Thiên
print('2. Lọc ra các bản ghi bán nhà riêng tại phường Trung liệt hoặc phường Khâm Thiên')
# phuong = df.query('('type_of_land' == 'Bán nhà riêng') and (('ward_name' == 'Phường Trung Liệt') or ('ward_name' == 'Phường Khâm Thiên')))

phuong = df[(df['type_of_land'] == 'Bán nhà riêng') & ((df['ward_name'] == 'Phường Trung Liệt') | (df['ward_name'] == 'Phường Khâm Thiên'))]
truycap_phuong = phuong.loc[:,['title','type_of_land','ward_name']]
print(truycap_phuong)
print('==============\n')


#3. Lọc các thông tin Địa chỉ, Giá, Hướng nhà, Hướng ban công của các bản ghi có giấy chứng nhận sổ đỏ và có 3 phòng ngủ trở lên.
print('3. Lọc các thông tin Địa chỉ, Giá, Hướng nhà, Hướng ban công của các bản ghi có giấy chứng nhận sổ đỏ và có 3 phòng ngủ trở lên')
thongtin = df[(df['land_certificate'] == 'Sổ đỏ') & (df['bedroom'] >=3)]
thongtin1 = thongtin.filter(['address','price','bedroom','land_certificate'])
print(thongtin1)
print('==============\n')


#4. Với mỗi loại nhà đất, tính trung bình cộng giá cũng như giá lớn nhất và giá nhỏ nhất.
print('4. Với mỗi loại nhà đất, tính trung bình cộng giá cũng như giá lớn nhất và giá nhỏ nhất')
giaTB = df.pivot_table(values = 'price', index = 'type_of_land', aggfunc = 'mean')
print(giaTB)
print('--------')

giamax = df.pivot_table(values = 'price', index = 'type_of_land', aggfunc = 'max')
print(giamax)
print('--------')

giamin = df.pivot_table(values = 'price', index = 'type_of_land', aggfunc = 'min')
print(giamin)
print('==============\n')

#5. Tính trung bình cộng số phòng ngủ, số phòng vệ sinh, số tầng của mỗi phường.
print('5. Tính trung bình cộng số phòng ngủ, số phòng vệ sinh, số tầng của mỗi phường')

chisoTB = df.pivot_table(values = ['bedroom','toilet','floor'], index = 'ward_name', aggfunc = 'mean')
print(chisoTB)