a=eval(input("输入a"))
b=eval(input("输入b"))
try:
    c=a/b
    print("a/b=",c)
except ZeroDivisionError :
    print("分母为零不合法")
except (ValueError, TypeError):
    print("输入不合法")
finally :
    print("程序已执行")



xhh=input(" ")
