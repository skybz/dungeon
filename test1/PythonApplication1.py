import mob
import room
import fa
import level
#初始化主角
me=mob.Mob(100,10,10,0,0)
#关于关卡的选择变量
i=1
while( i==0 or i==1):
    #如果是有怪物的就返回了怪物，没有怪物就返回了None
    enemy=level.got(i,me)
    i=i-1
    if enemy!=None:
        print('round start')
        while 1:
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
                break
            temp=enemy.attack-me.defense
            if temp<=0:
                temp=1
            me.health=me.health-temp
            if me.health<0:
                me.health=0
            print('you are caused %d damage' %temp,'you have %d health'%me.health)
            if me.health<=0:
                print('you died')
                break


    

    
