import my_class
import fa
import level
import sys
import random
#初始化变量这里要能读入文件
pass
total_score=0
game_times=0
higest_score=0
finsh_times=0
playing=0
xp_level=[5,7,10,25,60,99999]
#开始游戏
while(1):
    print('main menu')
    print('what do you want to do')
    print('1:start game')
    print('2:exit')
    while(1):
        m=input()
        m=int(m)
        if m==1:
            break
        if m==2:
            sys.exit(0)
        if m==3:
            print('error')
            continue
#初始化主角
    if playing==0:
        me=my_class.Mob(100,100,10,0,0)
        me.coin=0
        me.xp=0
        me.level=1
        me.itemsnum_1=10#生血药
        me.itemsnum_2=10#能量药
        me.itemsnum_3=10#爆炸弹（给敌人造成20点伤害）
        me.itemsnum_4=10#烟雾弹
        me.itemsnum=0#道具总量（背包总量）
        me.blessing_1=0
        me.blessing_2=0
    if playing==1:
        pass
#关于关卡的选择变量  
    i=0#目前在进行第几关
#地图数组存储
    round=0
    map=[1,2,0,0]
    vis=[0,0,0,0]
    num_level=4#地图里有多少关
    for i in range(num_level):
        temp=random.randint(0,num_level-1)
        while vis[temp]==1:
            temp=temp+1
            if temp>=num_level:
                temp=temp-num_level
        map[i]=temp      
        vis[temp]=1
    i=0
#退出标识
    flag_exit=0
    while( i <num_level):
     #如果是有怪物的就返回了怪物，没有怪物就返回了None
        if(me.health<=0):
            break
        playing=1
        if flag_exit==1:
            break
        enemy=level.got(map[i],me)
        i=i+1
        if enemy!=None:
            enemy.health=enemy.max_health
            round=0
            print('round start')
            print('your enemy is %s'%enemy.name)
            while 1:
                round=round+1
                if enemy.health==0 or me.health==0:#战斗结束
                #这里存档
                    pass#主角的所有属性
                    if enemy.health==0:
                    #主角的升级
                        me.coin=me.coin+enemy.coin
                        me.xp=me.xp+enemy.xp
                        while me.xp>=xp_level[me.level]:
                            print('your level has promted')
                            me.max_health=me.max_health+10
                            me.health=me.health+10
                            me.attack=me.attack+5
                            me.defense=me.defense+5
                            me.xp=me.xp-xp_level[me.level]
                            me.level=me.level+1
                            print('your ability has been strghten')
                    #playing=1
                        print('接下来你要：')
                        print('1.下一关')
                        print('2.离开')
                        temp_next=input()
                        temp_next=int(temp_next)
                        while 1:
                            if temp_next==1:
                                 break
                            if temp_next==2:
                                flag_exit=1
                                break
                            temp_next=input()
                            temp_next=int(temp_next)
                    if me.health==0:
                        pass
                    break
                print('plesase choose your mode:')
                m=input()
                m=int(m)
                temp=fa.cope(m,me,enemy) 
                if temp==-1:
                    print('you escaped')
                    break
                if me.health<=0:
                    print('you died\n')
                    playing=0
                    break
                enemy.health=enemy.health-temp
                if enemy.health<0 and temp!=0:
                    enemy.health=0
                print('you caused %d damage' %temp,'your enemy have %d health'%enemy.health)
                if enemy.health<=0:
                    print('you win')
                    continue
                temp=fa.copeb(round,me,enemy)
                if temp<=0:
                    temp=1
                me.health=me.health-temp
                if me.health<0:
                    me.health=0
                print('you are caused %d damage' %temp,'you have %d health'%me.health)
                if me.health<=0:
                    print('you died\n')
                    playing=0
                    break
    if(i==num_level):
        playing=0
        print('you finshed\n')

    

    
