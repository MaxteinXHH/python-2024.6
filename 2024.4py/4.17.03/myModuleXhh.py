def irn(a):
    b=int(a)
    c=(int(a[0]))**4+(int(a[1]))**4+(int(a[2]))*4+(int(a[3]))*4
    if b==c :
        return "是四叶玫瑰树"
    else:
        return "不是四页玫瑰树"

def isn(n):
    t=int(n[0])
    m=int(n[1])
    k=int(n[2])
    l=int(n[3])
    if t==l and m==k :
        return "是对称数"
    else :
        return "不是对称数"



