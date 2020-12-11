import my_class
import fa
import level
#初始化变量这里要能读入文件
total_score=0
game_times=0
higest_score=0
finsh_times=0
#这个变量不用存储检测是否在游戏中
playing=0
#初始化主角
playing=1
me=my_class.Mob(100,10,10,0,0)
#关于关卡的选择变量
i=0
#地图数组存储
map=[0,1]
num_level=2
#退出标识
flag_exit=0
while( i <num_level):
    #如果是有怪物的就返回了怪物，没有怪物就返回了None
    if flag_exit==1:
        break
    enemy=level.got(map[i],me)
    i=i+1
    if enemy!=None:
        print('round start')
        while 1:
            if enemy.health==0 or me.health==0:
                #这里存档
                pass
                if enemy.health==0:
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
                if me.health==0:
                    pass
                break
            print('plesase choose your mode:')
            m=input()
            m=int(m)
            temp=fa.cope(m,me,enemy)
            enemy.health=enemy.health-temp
            if enemy.health<0:
                enemy.health=0
            print('you caused %d damage' %temp,'your enemy have %d health'%enemy.health)
            if enemy.health<=0:
                print('you win')
                continue
            temp=enemy.attack-me.defense
            if temp<=0:
                temp=1
            me.health=me.health-temp
            if me.health<0:
                me.health=0
            print('you are caused %d damage' %temp,'you have %d health'%me.health)
            if me.health<=0:
                print('you died')
                continue

    

    
