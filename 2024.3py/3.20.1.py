import random
n=eval(input("输入n的值！"))
i=1
j_0=0
j_1=0
while i<=n:
    k=random.randint(0,1)
    i +=1
    if k==0:
        j_0 +=1
    else:
        j_1 +=1
print(f"0的次数是：{j_0}，1的次数是：{j_1}")
