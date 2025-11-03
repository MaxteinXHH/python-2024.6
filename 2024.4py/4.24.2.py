import re
a=input("输入您的用户名")
pa=r'^60\d{5}[BP]$'
if re.match(pa,a):
    print(f"您的工号是{a}")
else:
    print("用户名不存在！")







hh=input(" ")
