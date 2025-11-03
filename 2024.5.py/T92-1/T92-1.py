def isprime(r):
    if r<=1:
        return False
    else:
        for i in range(2,r):
            if r%i==0:
                return False
        return True
set1=set()  
with open("data.txt",'r',encoding="utf-8") as file:
    for jj in file:
        jj=int(jj.strip())
        if isprime(jj):
            set1.add(jj)
with open("prime.txt",'a',encoding="utf-8") as file2:
    for i in set1 :
        file2.write(str(i)+'\n')
            
