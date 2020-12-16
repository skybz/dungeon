#战斗函数中主角攻击函数
def cope(a,b,c):
    b.itemsnum=b.itemsnum_1+b.itemsnum_2+b.itemsnum_3+b.itemsnum_4
    while(1):
        if a==1:
            temp=1.5*b.attack-c.defense
            b.energy=b.energy+10
            temp=int(temp)
            if temp<=0:
                temp=1
            return temp
        if a==2:
            temp2=0.7*b.attack-c.defense
            b.energy=b.energy+10
            if temp2<=0:
                temp2=1
            temp=temp2*2
            temp=int(temp)
            return temp
        if a==3:
            if b.itemsnum!=0:
                print('which item do you want to use')
                print('''1:生血药
2:能量药
3:爆炸弹（给敌人造成20点伤害）
4:烟雾弹
5:返回''')
                while 1:
                    temp=input()
                    temp=int(temp)
                    if temp==1:
                       if(b.itemsnum_1<=0):
                           print('you don''t have this item')
                           continue
                       b.health=b.health+10
                       b.itemsnum_1=b.itemsnum_1-1
                       if b.health==b.max_health+10:
                           print('your health has been the maxminm')
                           b.itemsnum_1=b.itemsnum_1+1
                       if b.health>b.max_health:
                           b.health=b.max_health
                       print('your health is %d'%b.health)
                       print('your item left %d'%b.itemsnum_1)
                       break
                    if temp==2:
                       if(b.itemsnum_2<=0):
                           print('you don''t have this item')
                           continue
                       b.energy=b.energy+20
                       b.itemsnum_2=b.itemsnum_2-1
                       if b.energy>=100:
                           temp2=b.energy-100
                           b.energy=100
                           if temp2==0:
                               b.itemsnum_2=b.itemsnum_2+1
                               print('you energy has been the maxminm')
                               print('your item left %d'%b.itemsnum_2)
                               continue
                       print('your energy is %d'%b.energy)
                       print('your item left %d'%b.itemsnum_2)
                       break
                    if temp==3:
                        if(b.itemsnum_3<=0):
                            print('you don''t have this item')
                            continue
                        c.health=c.health-20
                        if c.health<0:
                            c.health=0
                        print('you caused 20 damage your enememy has %d health'%c.health)
                        break
                    if temp==4:
                        if(b.itemsnum_4<=0):
                            print('you don''t have this item')
                            continue
                        b.itemsnum_4=b.itemsnum_4-1
                        return -1                      
                    if temp==5:
                        b.itemsnum=b.itemsnum_1+b.itemsnum_2+b.itemsnum_3+b.itemsnum_4
                        break
                    print('error please rein')
            else:
                print('No item')
            if(c.health<=0):
                return 0
        if a==4:
            if(b.energy>=100):
                b.energy=0
                #旋风斩
                if b.blessing_1==1:
                    temp=3*(4*b.attack-c.defense)
                #以血还血
                elif b.blessing_2==1:
                    temp=15*b.attack-c.defense
                    b.health=b.health-5
                else:
                    temp=4*b.attack-c.defense
                temp=int(temp)
                if temp<=0:
                    temp=1
                return temp
            else:
                print('能量不足')
        print('please choose your mode')
        a=input()
        a=int(a)
#战斗中敌人的攻击函数
def copeb(round,me,enemy):
    if enemy.name=='slime_king':
        if round%3==1:
            print('slime_king decided to hit you heavily')
            return enemy.attack*1.5-me.defense
        if round%3==2:
            print('slime_king decided to hit you many times')
            return (enemy.attack-me.defense)*2
        if round%3==0:
            print('slime_king choose to use its ulimate hit')
            return enemy.attack*2.5-me.defense
    print('%s decided to hit you'%enemy.name)
    return enemy.attack-me.defense
    
