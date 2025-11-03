namelist=['安鑫','白雪','蔡玲玲','黄铭','张丹丹']
gradelist=[72,56,90,88,65,53]
a=zip(namelist,gradelist)
a=list(a)
print(a)
a.sort(key=lambda x:x[1],reverse=True)
print("\n\n\n\n降序后：\n\n",a)






gfd=input("")
