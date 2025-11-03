import keyword
import re

para=('test','int','12ab','a12b','if','def','a成分','_12a','1_2a','计算机成绩','a12345687900b')

p=r'^[a-zA-Z_]\w{0,9}$'

k=keyword.kwlist
for i in para:
    if re.search(p,i):
        for j in k:
            if j==k:
                o=0
                break
        
        print(i,"合法")
    else:
        o=0




hh=input("  ")
