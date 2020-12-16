import my_class
#在这里建立关卡
slime=my_class.Room(1)
eef=my_class.Room(2)
slime_king=my_class.Room(1)
teacher=my_class.Room(2)
level=[slime,eef,slime_king,teacher]
#对怪物的初始化方式
slime.a=my_class.Mob(0,0,0,0,0)
slime.a.name='slime'
slime.a.max_health=500
slime.a.health=slime.a.max_health
slime.a.attack=50
slime.a.defense=5
slime.a.crit_rate=0
slime.a.coin=10
slime.a.xp=10
#对boss的初始化方式
slime_king.a=my_class.Mob(0,0,0,0,0)
slime_king.a.name='slime_king'
slime_king.a.max_health=1000
slime_king.a.attack=20
slime_king.a.denfense=0
slime_king.a.crit_rate=0
slime_king.a.coin=20
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
            print('你当前最大生命值为%d,当前生命值为%d'%m.max_health%m.health)
            break
        else: 
            print('error')
eef.b=plot_eef
#对teacher的初始化
def plot_teacher(m):
    print('你遇到一位技术高超的勇士，他愿意教你他两种绝技中的一项，你选择：')
    print('1.旋风斩，你的绝技变为旋风斩（400%x3）')
    print('2.以血还血，你的绝技变为以血还血（1500%x1 但你会损失5点生命值）')
    while(1):
        temp=input()
        temp=int(temp)
        if temp==1:
            m.blessing_1=1
            print('你学会了旋风斩')
            break
        elif temp==2:
            m.blessing_2=1
            print('你学会了以血还血')
            break
        else: 
            print('error')
teacher.b=plot_teacher
#以上为初始化
#以下返回通过判断类型决定返回值
def got(x,people):
    if level[x].type==1:
        return level[x].a
    if level[x].type==2:
        level[x].b(people)
        return None
        