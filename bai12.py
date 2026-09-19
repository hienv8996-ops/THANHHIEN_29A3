import math

a = float(input('nhập a: '))
b = float(input('nhập b: '))
x = float(input('nhập x: '))
y = float(input('nhập y: '))
R = float(input('nhập bán kính r: '))
ket_qua = math.sqrt((x-a)**2+(y-b)**2)<=R * 2
print(ket_qua)
