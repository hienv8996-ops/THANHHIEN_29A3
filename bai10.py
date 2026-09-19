a = float(input('nhập a: '))
b = float(input('nhập b: '))
if a ==b:
    if b == 0:
        print('phương trình vô số nghiệm')
    else:
         print('phương trình vô nghiệm')
else:
    x = -b/a
print('in phương trình x: ',x)