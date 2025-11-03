import re
a=input("任意输入一段字符")
pa=r".*VB.*"
if re.match(pa,a):
    s=re.sub('VB','Python',a)
    print(s)
else :
    print("无替换内容")









l=input(" ")
