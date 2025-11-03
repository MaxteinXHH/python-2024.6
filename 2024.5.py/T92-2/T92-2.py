fiie=open("passornot.txt",'a',encoding="utf-8")
with open("grade.txt","r",encoding="utf-8") as filea:
    jj=0
    str0=filea.readline()
    fiie.write(str0)
    for i in filea:
        jj+=1
        if jj!=1 :
            str=[]
            str1=i.strip().split()
            if int(str1[3])>=60 and int(str1[2])>=60:
                str1.append("及格")
            else:
                str1.append("不及格")
            for hh in str1:
                fiie.write(hh+' ')
        fiie.write('\n')
fiie.close()
