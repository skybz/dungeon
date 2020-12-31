import my_class
import random
#在这里建立关卡 第一个空是类型第二个是分数
slime=my_class.Room(1,2)#1是怪物
eef=my_class.Room(2,1)#2是事件
slime_king=my_class.Room(1,4)#这是boss
teacher=my_class.Room(2,1)#事件
shop=my_class.Room(3,1)#2是商店
bird=my_class.Room(1,2)#1是怪物
blue_slime=my_class.Room(1,2)
undead_miners=my_class.Room(1,2)
coffin=my_class.Room(2,1)
root=my_class.Room(2,1)
witch=my_class.Room(2,1)
level=[slime,eef,teacher,bird,blue_slime,undead_miners,shop,slime_king]
#对怪物的初始化方式
slime.a=my_class.Mob(0,0,0,0,0)
slime.a.name='ghost'
slime.a.max_health=50
slime.a.health=slime.a.max_health
slime.a.attack=10
slime.a.defense=0
slime.a.crit_rate=0
slime.a.coin=17
slime.a.xp=14
slime.a.image='baddie4.png'
#初始化bird
bird.a=my_class.Mob(0,0,0,0,0)
bird.a.name='bird'
bird.a.max_health=100
bird.a.health=bird.a.max_health
bird.a.attack=8
bird.a.defense=0
bird.a.crit_rate=0
bird.a.coin=14
bird.a.xp=11
bird.a.image='baddie.png'
blue_slime.a=my_class.Mob(0,0,0,0,0)
blue_slime.a.name='blue_slime'
blue_slime.a.max_health=100
blue_slime.a.health=blue_slime.a.max_health
blue_slime.a.attack=15
blue_slime.a.defense=6
blue_slime.a.crit_rate=0
blue_slime.a.coin=16
blue_slime.a.xp=12
blue_slime.a.image='baddie3.png'
undead_miners.a=my_class.Mob(0,0,0,0,0)
undead_miners.a.name='undead_miners'
undead_miners.a.max_health=200
undead_miners.a.health=undead_miners.a.max_health
undead_miners.a.attack=18
undead_miners.a.defense=10
undead_miners.a.crit_rate=0
undead_miners.a.coin=100
undead_miners.a.xp=20
undead_miners.a.image='baddie2.png'
ghost=my_class.Mob(0,0,0,0,0)
ghost.name='ghost'
ghost.max_health=200
ghost.health=ghost.max_health
ghost.attack=8
ghost.defense=0
ghost.crit_rate=0
ghost.coin=10
ghost.xp=10
ghost.image='baddie.png'
#对boss的初始化方式
slime_king.a=my_class.Mob(0,0,0,0,0)
slime_king.a.name='slime_king'
slime_king.a.max_health=500
slime_king.a.attack=20
slime_king.a.denfense=0
slime_king.a.crit_rate=0
slime_king.a.coin=20
slime_king.a.xp=100
slime_king.a.image='slime.png'

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
#对棺材的初始化
def plot_coffin(a):
    print('''你遇到了一个棺材，你再想是否要打开它
1：打开它
2：绕开它''')
    while(1):
        temp=input()
        temp=int(temp)
        if temp==1:
            temp2=random.randint(0,1)
            if temp2==0:
                print('一股尸气从里面冒了出来，你的血量减少了10点')
                print('你当前血量为%d'%a.health)
                return ghost
            if temp2==1:
                print('you find a sword')
                a.attack=a.attack+10
                print('你的攻击力提升了10点现在为%d'%a.attack)
            break
        elif temp==2:
            print('nothing happened')
            break
        else: 
            print('error')
coffin.b=plot_coffin
#对商店初始化
def plot_shop(a):
    #objects=['health','energy','attack','defense']
    prices=[4,3,2,1]
    nums=[1,1,1,1]
    limit=[4,4,4,4]
    print('you have been in the shop')
    while 1:
        print('''输入0`4进行选择：
0：生血丸
1：能量药
2: 爆炸弹
3: 烟雾弹
4: 离开''')
        od=input()
        od=int(od)#od 指令 从0到3编号！！！
        if od==1:
            if a.coin<prices[0]:
                print("You can't pay for the object!")
            elif a.itemsnum_1==limit[od]:
                print("You don't have space for the object!")
            else:
                a.coin=a.coin-prices[0]
                a.itemsnum_1=a.itemsnum_1+1
                print("Your health has added!")
        if od==2:
            if a.coin<prices[od]:
                print("You can't pay for the object!")
            elif a.itemsnum_2==limit[1]:
                print("You don't have space for the object!")
            else:
                a.coin=a.coin-prices[1]
                a.itemsnum_2=a.itemsnum_2+1
                print("Your energy has added!")
        if od==3:
            if a.coin<prices[2]:
                print("You can't pay for the object!")
            elif a.itemsnum_3==limit[2]:
                print("You don't have space for the object!")
            else:
                a.coin=a.coin-prices[2]
                a.itemsnum_3=a.itemsnum_3+1
                print("Your attack has added!")
        if od==4:
            if a.coin<prices[3]:
                print("You can't pay for the object!")
            elif a.itemsnum_4==limit[3]:
                print("You don't have space for the object!")          
            else:
                a.coin=a.coin-prices[3]
                a.itemsnum_4=a.itemsnum_4+1
                print("Your defense has added!")
        if od==5:
            break
shop.b=plot_shop
def plot_witch(m):
    print('你遇到了一个女巫，她威胁你喝掉一瓶毒药，你选择：')
    print('1.软骨散（攻击力减少6）')
    print('2.慢性毒药（最大生命值减少10）')
    while(1):
        temp=input()
        temp=int(temp)
        if temp==1:
            m.attack=m.attack-6
            print('你当前攻击力为%d'%m.attack)
            break
        elif temp==2:
            m.max_health=m.max_health-10
            m.health=m.health-10
            print('你当前最大生命值为%d,当前生命值为%d'%(m.max_health ,m.health))
            break
        else: 
            print('error')
witch.b=plot_witch
def plot_root(m):
    print('你遇到了一个空心树根，它挡住了你的路，你选择：')
    print('1.绕开它，继续向前走')
    print('2.劈开它（可能会得到宝物，但需消耗10攻击值）')
    while(1):
        temp=input()
        temp=int(temp)
        if temp==1:
            print('无事发生')
            break
        elif temp==2:
            m.max_health=m.max_health+12
            m.health=m.health+12
            print('你发现你的剑钝了，你得到了一瓶强心剂，最大生命值提高了12，目前最大生命值为%d，当前生命值为%d'%m.max_health%m.health)
            break
        else: 
            print('error')
root.b=plot_root
#以上为初始化
#以下返回通过判断类型决定返回值
def got(x,people):
    if level[x].type==1:
        return level[x].a
    if level[x].type==2:
        return level[x].b(people)
def getpoint(x):
    return level[x].point
def gettype(x):
    return level[x].type