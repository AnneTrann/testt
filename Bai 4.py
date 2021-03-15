"""

# tat ca cac dong Ctrl + /
ds_so_nguyen_duong = [2,3,4,5,3,5,6,8,9,0]
for i in ds_so_nguyen_duong:
    print(i)

tong=0
ds_so_nguyen_duong = [2,3,4,5,3,5,6,8,9,0]
for i in ds_so_nguyen_duong:
    tong+=i
print(tong)

#giai phuong trinh ax+b=0
a=int(input("Nhập giá trị a: "))
b=int(input("Nhập giá trị b: "))
for i in range (0,100): #dc nhap lai a=0 100 lan #range(100)=range(0,100)
    if a==0:
        print("Vui long nhap gia tri a khac 0")
        a=int(input("Nhập giá trị a: "))
        #i=1 lap lai ko gioi han so lan nhap a=0
    else:
        print(-b/a)
        break #thoát khỏi vòng lặp

# cho ds1=[1,2,3],ds2=[2,3,0] xuất ra kq [3,5,3]
ds1=[1,2,3,5]
ds2=[2,3,0,2]
ds3=[]
for i in range(0,len(ds1)):
    ds3.append(ds1[i] + ds2[i])
print(ds3)
# cộng ds1 dài hơn ds2
ds1=[1,2,3,5,7]
ds2=[2,3,0]
ds3=[]
l1=len(ds1)
l2=len(ds2)
if l1>l2:
    for i in range(0,l1-l2):
        ds2.append(0)
if l1<l2:
    for i in range(0,l2-l1):
        ds1.append(0)
for j in range(0,len(ds1)):
    ds3.append(ds1[j] + ds2[j])
print(ds3)


#nghĩa là truy cập hàm sql trong function của file math.py, * tất cả mọi hàm trong math.py
from math import * #nếu ko có dòng này mà truy xuất sqrl thì bị lỗi : name 'sqrt' is not defined
#nếu chỉ import sqrt mà ko import * thì nó chỉ chạy đúng dòng sqrt, dòng hàm khác nếu cùng nằm trong math ko chạy đc
can_delta=sqrt(9) #can_delta là biến
print(can_delta)
gia_tri_tuyet_doi=abs(-5)
print(gia_tri_tuyet_doi)
cos=cos(90)
print(cos)

"""


ds1 = [1,2]
ds2 = [9,1,9]
#kq trả về là [0,4,9]

# cách 1
ds3 = []
dss = []

l1 = len(ds1)
l2= len(ds2)

if l1>l2:
    for i in range(0,l1-l2):
        ds2.append(0)
elif l1<l2:
    for i in range(0,l2-l1):
        ds1.append(0)

print(ds1)
print(ds2)

for j in range(0,len(ds1)):
#cho j chạy từ 0 đến len(ds nào cũng đc, do đã cân len(ds1)=len(ds2), nếu ko để len thì sẽ
# bị sai cú pháp nếu th l2>l1
    dss.append(ds1[j]+ds2[j])
    print(dss)
print(dss[0])

for n in range(0,len(dss)):
    dss[n]=dss[n]+temp #trc khi chạy vòng lặp thì cộng temp trc
    temp=0 # reset temp sau khi đã cộng, ko update temp nữa
    if dss[n]>=10:
        ds3.append(dss[n]%10)
        temp=int(dss[n]/10)
    else:
       ds3.append(dss[n])

if temp>0:
    ds3.append(temp)
print(ds3)

# cách 2
ds1=[0,0,0]
ds2=[2,3,11]
ds3=[]
ds4=[]
if len(ds1) < len(ds2):
    for i in range(0,len(ds2)-len(ds1)):
        ds1.append(0)

elif len(ds1) > len(ds2):
    for i in range(0,len(ds1)-len(ds2)):
        ds2.append(0)

for j in range(0,len(ds1)):
    ds3.append(ds1[j]+ds2[j])

print(ds3)
for i in range(0,len(ds3)):
    ds4.append(ds3[i]%10)
    if i+1<len(ds3):
            ds3[i+1]=ds3[i+1]+ds3[i]//10
    else:
            break
if ds3(len(ds3)-1)>=10:
    ds4.append(ds3[len(ds3)-1]//10)
print(ds4)

#in ra dãy số tăng dần từ 0 đến 10
i=0
while i<10:
    print("gia tri i la:",i)
    i+=1

i=0
while i<10:
    print("gia tri i la:",10-i)
    i+=1

#kiem tra một số có phải số nguyên tố không?
n=int(input("Nhập một số tự nhiên: "))
dem=0
i=1
while i<n:
    i=i+1
    if n%i==0:
        dem=dem+1
if dem>1:
    print (n, " không là số nguyên tố")
else:
    print(n," là số nguyên tố")

#or
b =int(input("Nhập một số"))
dem=0
i=2
while i<b:
    if b%i == 0:
      dem+=1
    i = i +1
print(dem)
if dem>0:
    print(b,"khong là một số nguyên tố")
else:
    print(b,"là số nguyên tố")


for i in range (0,10):
    if i ==8:
        continue
    else:
        print(i)
    print("ahja",i)
for i in range (0,10):
    if i ==8:
        break
    else:
        print(i)
    print("jhqkjq",i)
#continue và break đều CHỈ có tác dụng TRONG for và while, bên ngoài và bên trong thì ko liên quan
