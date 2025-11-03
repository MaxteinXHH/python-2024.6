y=input("输入四位正整数")
g=int(y)
if g>=1000 and g<=10000 and g==a**4+b**4+c**4+d**4 :
    a=int(y[0])
    b=int(y[1])
    c=int(y[2])
    d=int(y[3])
    print("是四叶玫瑰数！")
else:
    print("不是四叶玫瑰数！")
