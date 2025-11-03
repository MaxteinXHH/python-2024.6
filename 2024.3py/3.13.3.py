x=eval(input("输入x"))
if x<-6:
    y=4*x
elif x<1 and x>=-6:
    y=(3*x)/(x-2)
else:
    y=x*x*x
y=round(y,3)
print("y的值为",y)
