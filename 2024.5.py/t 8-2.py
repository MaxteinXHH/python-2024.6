def box(c,w,h):
    for e in range(h):
        for i in range(w):
            if i==w-1:
                print(c,end="\n")
            else:
                print(c,end=' ')
a=input("输入字符")
b=eval(input("输入宽"))
c=eval(input("输入高"))
try:
    d=1
    if len(a)==1 and b>2 and c>2 :
        f=box(a,b,c,)
        d=9
except TypeError :
    d=1
if d==1:
    print("输入不合理")




xhh=input(" ")
    
    

        
        
