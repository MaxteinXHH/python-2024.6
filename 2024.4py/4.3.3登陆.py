a={'admin': '123456ad' ,'abc': '12345_67q','user2': 'haha2345'}

bp=0
i=0
j=0
for q in range(11):
    if q==10 and j !=23 :
        print("\n用户名输错10次了！洗洗睡吧\n")
    else:
        if j==23:
            break
        else:
            c=input(f"\n输入用户名.no.{q+1}.....")
            for key in a.keys() :
                bp+=1
                if key ==c :
                    d=a.get(key)
                    for i in range(5):
                         b=input(f"\n输入密码..{i+1}....")
                         if b==d:
                            print("\n登陆成功！")
                            j=23
                            break
                         else:
                             if i==4:
                                 print("\n登录失败5次！")
                                 break
                             else:
                                 print("\n登录失败")
                else:
                    if j==23:
                        break
                    else:
                        if bp==3:
                            if i==4:
                                print("\n重新输入用户名！")
                                i=0
                            else:
                                print("\n用户名不存在！")
                                print("\n重新输入用户名！")
                            bp=0








dDafg=input("   ")
                    
    
