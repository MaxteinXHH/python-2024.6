import math
a=input("输入任意自然数")
b=a[ : :-1]
a=int(a)
b=int(b)
if a==b:
    print(a,"是回文数！")
else:
    print(a,"不是回文数！")
