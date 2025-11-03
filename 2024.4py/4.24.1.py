import re
stra="abcd"
Stra=stra.upper()
print(Stra)

sa="cd"
strr=stra.find(sa)
print(strr)

stra="a,b,c,d"
stt=re.split(',',stra)
print(stt,type(stt))

stra="Python is good"
stra2=re.sub('P','p',stra)
print(stra2)


stra="python字符串正则表达式.html"
sds=re.match(r'(.*)\.html',stra).group(1)
print(sds)


stra="this is a book"
st1=re.sub('book','apple',stra)
print(st1)


stra="this is a book"
par=stra.startswith('this')
if par==True :
    print("yes")


stra="this is a apple"
par=stra.endswith('apple')
if par==True:
    print("yes")

stra="this is a book\n"
st2=re.sub('\n','',stra)
print(st2)
















hh=input(" ")
