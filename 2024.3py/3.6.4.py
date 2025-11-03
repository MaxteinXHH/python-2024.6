import math
a=input("输入a")
b=input("输入b")
c=input("输入c")
a=int(a)
b=int(b)
c=int(c)
e=b*b-4*a*c
if e>=0:
    e=math.sqrt(e)
    x_1=(-b+e)/(2*a)
    x_2=(-b-e)/(2*a)
    if x_1==x_2:
        print("有唯一实根",x_1)
    else:
        print("有实根X_1=",x_1,"X_2=",x_2)
else:
    print("无实根！")
