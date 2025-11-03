import random
n=eval(input("输入n"))
if n<1:                         # 不小于1 
    print("建议n>=100")
    n=eval(input("输入n"))
x=0
y=0
i=0
while i< n :
    a= random.randint(0,1)
    i+=1
    if a==0:
        x+=1
    else:
        y+=1
print(f"0出现了{x}次，1出现了{y}次")




a=input("")   #保留窗口
        
