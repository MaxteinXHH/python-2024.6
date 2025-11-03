n=eval(input("输入购买数量"))
if n==1:
    p=198
elif n==2:
    p=198*0.9*2
elif n==3:
    p=198*3*0.8
else:
    p=198*n*0.7
p=round(p,3)
print("消费金额为",p)
        
