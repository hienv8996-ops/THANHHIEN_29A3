import math
a = float(input('nhập a: '))
b = float(input('nhâp b: '))
c = float(input('nhâp c: '))
if a + b <= c or b + c <= a or a + c <= b:
    print('không là tam giác')
else:
    if a == b and b == c:
        print('tam giác đều')
    elif a == b or a == c or b == c and a ** a + b ** b == c ** c or a ** a + c ** c == b ** b or b ** b + c**c == a ** a:
        print('tam giác vuông cân')
    elif a == b or a == c or b == c:
        print('tam giác cân')
    elif a * a + b * b == c * c or a * a + c*c == b * b or b * b + c * c == a * a:
        print('tam giác vuông')
    else:
      print('tam giác thường')