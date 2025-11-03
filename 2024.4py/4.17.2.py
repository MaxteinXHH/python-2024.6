listch=['12','78','-69','108','-2','36','5','3','-90','8']

#1

def s1(m):
    m=int(m)
    return m
f1=map(s1,listch)
listnum=list(f1)
print(listnum,"\n\n")

#2

def s2(n):
    if n%2==0 and n%3==0 :
        return True
    else:
        return False
f2=filter(s2,listnum)
listcon23=list(f2)
print(listcon23,"\n\n")

#3

from functools import reduce
def s3(a,b):
    c=a+b
    return c
f3=reduce(s3,listnum)
print(f3,"\n")

#4

f4=sorted(listnum,key=abs,reverse=True)
f5=list(f4)
print(f5,"\n")






aiop=input(" ")

