def multiply(*ha) :
    h=1
    for i in ha :
        i=int(i)
        h=h*i
    return h
a=input("输入任意个数字，请以空格分开，以计算乘积")
a=a.split()
f=multiply(*a)
print(f)







hi=input(" ")
