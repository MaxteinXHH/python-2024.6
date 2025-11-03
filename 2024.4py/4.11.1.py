def ha(a) :
    if a%2==0 and a%7==0 :
        return True
    else :
        return False
b=eval(input("输入正整数以判断"))
c=ha(b)
print(c,"\n200-1000内符合条件的数有：")
for i in range(200,1001):
    b=ha(i)
    if b==True :
        print(i,end=" ")





gh=input("  ")

