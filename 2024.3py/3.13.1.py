n=eval(input("输入年份"))
if (n%4==0 and n%100!=0) or n%400 ==0:
    print(n,"是闰年")
else:
    print(n,"不是闰年！")
