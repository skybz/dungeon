import my_class
#在这里建立关卡
smile=my_class.Room(1)
eef=my_class.Room(2)
level=[smile,eef]
#对怪物的初始化方式
smile.a=my_class.Mob(0,0,0,0,0)
smile.a.max_health=100
smile.a.health=smile.a.max_health
smile.a.attack=10
smile.a.defense=5
smile.crit_rate=0
#对事件初始化方式
def plot_eef(m):
    print('你遇到了一个小精灵，它愿意给你它的一个宝物，你选择：')
    print('1.强力剂（攻击力提高5）')
    print('2.强心剂（最大生命值提高7）')
    while(1):
        temp=input()
        temp=int(temp)
        if temp==1:
            m.attack=m.attack+5
            print('你当前攻击力为%d'%m.attack)
            break
        elif temp==2:
            m.max_health=m.max_health+7
            m.health=m.health+7
            pritnt('你当前最大生命值为%d,当前生命值为%d'%m.max_health%m.health)
            break
        else: 
            print('error')
eef.b=plot_eef
#以上为初始化
#以下返回通过判断类型决定返回值
def got(x,people):
    if level[x].type==1:
        return level[x].a
    if level[x].type==2:
        level[x].b(people)
        return None
        