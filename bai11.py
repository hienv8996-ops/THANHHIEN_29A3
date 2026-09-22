import math
a = float(input('nhập a: '))
b = float(input('nhập b: '))
c = float(input('nhâp c: '))
if a ==0:
    print('không phải phương trình bậc 2')
else:
    delta= b*b-4*a*c
    if delta<0:
        print('phương trình vô nghiệm')
    elif:
        x=-b/(2*a)
        print('phương trình có nghiệm kép')
    else:
        x1=(-b + math.sqrt(delta))/(2*a)
        x2=(-b - math.sqrt(delta))/(2*a)
        print('phương trình có 2 nghiệm: ')
        print('x1 = ',x1)
        print('x2 = ',x2)
