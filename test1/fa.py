def cope(a,b,c):
    while(1):
        if a==1:
            temp=1.5*b.attack-c.defense
            temp=int(temp)
            if temp<=0:
                temp=1
            return temp
        if a==2:
            temp2=0.7*b.attack-c.defense
            if temp2<=0:
                temp2=1
            temp=temp2*2
            temp=int(temp)
            return temp
        if a==4:
            if(b.energy>=100):
                b.energy=0
                temp=4*b.attack-c.defense
                temp=int(temp)
                if temp<=0:
                    temp=1
                return temp
            else:
                print('能量不足')
        print('请重新输入')