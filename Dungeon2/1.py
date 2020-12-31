import pygame,time,sys,random
from pygame.locals import *
import my_class,level,saveload,os,fa
WINDOWWIDTH = 640
WINDOWHEIGHT = 360
CARDWIDTH = 110
CARDHEIGHT = 150 #卡牌高度
BATTLEINFO_H = 50 #战斗信息栏高度
Info_Key_Size = 30#信息栏里每一项的大小
FPS = 60

pygame.init()
mainClock = pygame.time.Clock()
#加载声音
pygame.mixer.music.set_volume(0.5)
clickSound = pygame.mixer.Sound('SOTE_SFX_UIClick_1_v2.wav')
buySound = pygame.mixer.Sound('买东西.ogg')
startSound = pygame.mixer.Sound('开始游戏.ogg')
eventSound = pygame.mixer.Sound('进入事件.ogg')
playerSound = pygame.mixer.Sound('人物攻击.ogg')
baddieSound = pygame.mixer.Sound('怪物攻击.ogg')
bloodSound = pygame.mixer.Sound('回血.ogg')#回血的音效
VictorySound = pygame.mixer.Sound('主界面音乐.ogg')#胜利之后的音乐
DefeatSound = pygame.mixer.Sound('主角死亡.ogg')
bombSound = pygame.mixer.Sound('爆炸.ogg')#爆炸药
attackSound = pygame.mixer.Sound('加攻击.ogg')#加攻击的音效
defenseSound = pygame.mixer.Sound('加防御.ogg')#加防御的音效
energySound = pygame.mixer.Sound('加能量.ogg')#加能量的音效
cardSound = pygame.mixer.Sound('SOTE_SFX_CardSelect_v2.ogg')

#Colors
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
Teal = (0, 128, 128)
Purple = (128, 0, 128)
LIME = (0, 128, 0)
GREY = (128, 128, 128)
GOLD = (255, 215 , 0)
AZURE = (135, 206, 235)#天蓝色

#Surface
windowSurface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT), 0, 32)
start_Surface = pygame.Surface(windowSurface.get_size())
game_Surface = pygame.Surface(windowSurface.get_size())
store_Surface =  pygame.Surface(windowSurface.get_size())
event_surface =  pygame.Surface(windowSurface.get_size())


basicFont = pygame.font.SysFont('inkfree', 60)
small_Font = pygame.font.SysFont('inkfree', 15)
#player_im = 'player.png'
#定义卡组的数组
cards = []
card_names = ['card1.png','card2.png','card3.png']

#定义用药的按钮
drugs = []
drug1_rect = pygame.Rect(260,0,33,33)#血量
drugs.append(drug1_rect)
drug2_rect = pygame.Rect(310,0,30,30)#能量
drugs.append(drug2_rect)
drug3_rect = pygame.Rect(370,0,35,35)#爆炸
drugs.append(drug3_rect)
drug4_rect = pygame.Rect(420,0,30,30)#烟雾
drugs.append(drug4_rect)



def terminate():#用于退出的函数
    pygame.quit()
    sys.exit()

def Isin(x, y, rect):#判断(x,y)坐标是不是在矩阵里面
    if rect.left<=x and x<=rect.right and rect.top<=y and y<=rect.bottom and y<=WINDOWHEIGHT and y>=0:
        return True
    return False

def DrawBackground(bg_pic, surface):
    bg_Image = pygame.image.load(bg_pic)
    bg_StrechedImage = pygame.transform.scale(bg_Image,(WINDOWWIDTH,WINDOWHEIGHT))
    surface.blit(bg_StrechedImage, (0,0))
def DrawImage(image_name, surface, width, height, pos_x, pos_y):#后面两个参数表示左上角的位置
    image = pygame.image.load(image_name)
    image_Streched = pygame.transform.scale(image, (width, height))#设置大小
    rect_ = image_Streched.get_rect()
    rect_.topleft = (pos_x,pos_y)
    surface.blit(image_Streched, rect_) #画上去
    return rect_
def DrawSurface(surface):
    windowSurface.blit(surface, (0,0))
    pygame.display.update()
def DrawText(text, color,font, surface, x, y):#x,y表示中心位置
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.centerx = x
    textrect.centery = y
    surface.blit(textobj, textrect)
    return textrect


def Background(background):#开始界面
    Font2 = pygame.font.SysFont(None, 20)
    DrawBackground(background, start_Surface)
    DrawText('Topscore: %s'%(highest_score),WHITE,Font2,start_Surface,50,15)
    DrawText('Finish Times: %s'%(finsh_times),WHITE,Font2,start_Surface,60,35)
    pygame.display.set_caption('start')

    #DrawText('Dungeon', GOLD, basicFont, start_Surface, (WINDOWWIDTH/2),(WINDOWHEIGHT/3))
    DrawImage('panel.png',  start_Surface, 180 , 80  , 230  , 200)
    start_rect = DrawText('start',RED, basicFont, start_Surface,(WINDOWWIDTH/2),(2*WINDOWHEIGHT/3))
    
    DrawImage('panel.png',  start_Surface,  180  , 80  , 230  , 290)
    exit_rect = DrawText('exit',RED, basicFont, start_Surface,(WINDOWWIDTH/2),(2*WINDOWHEIGHT/3) + 90)
    
    DrawSurface(start_Surface)
    
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
               terminate()
            if event.type == MOUSEBUTTONUP:
                x,y = pygame.mouse.get_pos()
                if Isin(x,y, start_rect):
                    clickSound.play()
                    #Game('battle_1.jpg')
                    return 
                elif Isin(x,y, exit_rect):
                    clickSound.play()                   
                    terminate()
        
#战斗事件
def Game(battle_bg):#参数为战斗背景，函数功能为设置游戏界面
    pygame.display.set_caption('Battle')
    DrawBackground(battle_bg, game_Surface)#显示背景图
    #pygame.draw.rect(game_Surface, GREY,(0, 0, WINDOWWIDTH, BATTLEINFO_H))#绘制战斗信息栏
    #pygame.draw.line(game_Surface, BLACK, (320, 0), (320, 50), 4)
    DrawImage('bar.png',game_Surface,WINDOWWIDTH,50,0,0)
    #补充游戏信息
    DrawImage('energy.png',game_Surface,30,30,0,50)
    DrawText('Score  %s'%(score),WHITE,small_Font,game_Surface,30,90)
    DrawText('Lv.   %s'%(player.level),WHITE,small_Font,game_Surface,25,40)
    DrawImage('attack.png', game_Surface, Info_Key_Size+10, Info_Key_Size+10, 5, -5)
    DrawImage('health.png', game_Surface, Info_Key_Size, Info_Key_Size, 60, 0)
    DrawImage('defense.png', game_Surface, Info_Key_Size-5, Info_Key_Size-5, 150, 0)
    DrawImage('coin.png', game_Surface, Info_Key_Size, Info_Key_Size, 210, -3)

    DrawImage('血量.png',game_Surface,Info_Key_Size+3,Info_Key_Size+3, 260, -10)
    DrawImage('能量.png',game_Surface,Info_Key_Size,Info_Key_Size, 310, 0)
    DrawImage('爆炸.png',game_Surface,Info_Key_Size+5,Info_Key_Size+5, 370,-5)
    DrawImage('烟雾.png',game_Surface,Info_Key_Size,Info_Key_Size, 420, -2)
    
    DrawImage('health.png', game_Surface, Info_Key_Size, Info_Key_Size, 500, 0)
    #DrawImage('attack.png', game_Surface, Info_Key_Size+10, Info_Key_Size+10, 500, 50)
    #DrawImage('baddie1.png',game_Surface, 100, 100, 500 , 100)
    for i in range(3):
        cardRect = pygame.Rect(110+150*i, WINDOWHEIGHT - CARDHEIGHT*2/3, CARDWIDTH, CARDHEIGHT)
        cards.append(cardRect) #把每张牌的位置存下来
def DrawCards(x):#x表示不画的那张牌
   for i in range(3):
        if i!= x:
            DrawImage(card_names[i], game_Surface, CARDWIDTH, CARDHEIGHT, 
            110+150*i, WINDOWHEIGHT - CARDHEIGHT*2/3)
def DrawNum(Not_Draw):#显示各项能力的数值,Not_Draw表示暂时不显示的数值
    pass
    if Not_Draw !=1:
        DrawText('%s'%(player.attack),RED,small_Font,game_Surface,45,13)
    if Not_Draw !=2:
        DrawText('%s'%(player.health),RED,small_Font,game_Surface,100,13)
    if Not_Draw !=3:
        DrawText('/%s'%(player.max_health),RED,small_Font,game_Surface,130,13)
    if Not_Draw !=4:
        DrawText('%s'%(player.defense),AZURE,small_Font,game_Surface,190,13)
    if Not_Draw !=5:
        DrawText('%s'%(player.coin),GOLD,small_Font,game_Surface,250,13)
    if Not_Draw !=6:
        DrawText('%s'%(player.itemsnum_1),RED,small_Font,game_Surface,300,13)
    if Not_Draw !=7:
        DrawText('%s'%(player.itemsnum_2),RED,small_Font,game_Surface,350,13)
    if Not_Draw !=8:
        DrawText('%s'%(player.itemsnum_3),RED,small_Font,game_Surface,410,13)
    if Not_Draw !=9:
        DrawText('%s'%(player.itemsnum_4),RED,small_Font,game_Surface,450,13)
    if Not_Draw != 10:
        DrawText('%s'%(enemy.health),RED,small_Font,game_Surface,550,13)
    DrawText('/%s'%(enemy.max_health),RED,small_Font,game_Surface,580,13)
    if Not_Draw != 11:
        DrawText('%s'%(player.energy),AZURE,small_Font,game_Surface,40,63)
    DrawSurface(game_Surface)
def DrawEnemy(enemy_im):#将敌人画到默认位置
    DrawImage(enemy_im,game_Surface, 100, 100, 500 , 100)
def DrawPlayer(player_im):#将玩家画到默认位置
    DrawImage(player_im,game_Surface, 100, 100,100,100)
def Move_enemy(battle_bg,player_im,enemy_im,delta):#移动敌人,del表示伤害
    left = 500
    flag = False
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                terminate()
        if left >450 and not flag:
            left-=5
            Game(battle_bg)
            DrawCards(3)
            DrawPlayer(player_im)
            DrawNum(0)
            DrawImage(enemy_im,game_Surface,100,100,left,100)
            DrawSurface(game_Surface)
        if left == 450 and not flag:
            DrawImage(enemy_im,game_Surface,100,100,left,100)
            baddieSound.play()
            DrawScar(left,enemy_im,player_im,player,battle_bg,1)#画一下伤痕，以提升视觉体验
            Change_Health(battle_bg,player_im,enemy_im,left,100,13,player.health,delta,-1,1)
            #上面两个函数均表示受伤的一方是不是玩家
            time.sleep(0.5)
            left += 5
            flag = True
        if left < 500 and flag:
            left+=5
            Game(battle_bg)
            DrawCards(3)
            DrawNum(0)
            DrawPlayer(player_im)
            DrawImage(enemy_im,game_Surface,100,100,left,100)
            DrawSurface(game_Surface)
        if left == 500 and flag:
            return 
       
        mainClock.tick(FPS)
def Move_player(battle_bg,player_im,enemy_im,delta):#发动技能的时候移动玩家,delta表示伤害
    left = 100
    flag = False
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                terminate()
        if left < 150 and not flag:
            left+=5
            Game(battle_bg)
            DrawCards(3)
            DrawEnemy(enemy_im)
            DrawNum(0)
            DrawImage(player_im,game_Surface,100,100,left,100)
            DrawSurface(game_Surface)
        if left == 150 and not flag:
            DrawImage(player_im,game_Surface,100,100,left,100)
            playerSound.play()
            DrawScar(left,enemy_im,player_im,player,battle_bg,0)#画一下伤痕，以提升视觉体验
            Change_Health(battle_bg,player_im,enemy_im,left,550,13,enemy.health,delta,-1,0)
            time.sleep(0.5)
            left -= 5
            flag = True
        if left > 100 and flag:
            left-=5
            Game(battle_bg)
            DrawCards(3)
            DrawNum(0)
            DrawEnemy(enemy_im)
            DrawImage(player_im,game_Surface,100,100,left,100)
            DrawSurface(game_Surface)
        if left == 100 and flag:
            return 
       
        mainClock.tick(FPS)
def DrawScar(left,enemy_im,player_im,player,battle_bg,is_player):#画(玩家和敌人)伤痕
    #如果受伤的是玩家,is_player为1，反之为0
    if is_player:
        pos_x = 150
    else:
        pos_x = 500
    
    pos_y = 30
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                terminate()
        Game(battle_bg)
        DrawCards(3)
        DrawNum(0)

        if is_player:
            DrawPlayer(player_im)
            DrawImage(enemy_im,game_Surface,100,100,left,100)
        else:
            DrawEnemy(enemy_im)
            DrawImage(player_im,game_Surface,100,100,left,100)
        DrawImage('dagger.png',game_Surface,20,40,pos_x,pos_y)
        DrawSurface(game_Surface)
        if pos_y < 50:
            pos_y += 3
        else :
            time.sleep(0.5)
            return 
def Change_Health(battle_bg,player_im,enemy_im,left,pos_x,pos_y,ori_num,del_num,is_add,is_player):
    #改变(玩家和敌人的)血量
    #left表示敌人的x坐标,pox_s和pos_y表示数值在哪里,ori_num：原来的数,
    # del_num：变化了多少,is_add：是不是加（加为1，减为-1）
    #is_player表示受伤的是不是玩家
    num = ori_num
    goal = ori_num+del_num*is_add
    
    if is_add == 1 and goal > player.max_health:
        goal = player.max_health
        del_num = player.max_health - ori_num
    if is_add == -1 and goal < 0:
        goal = 0
        del_num = num
    
    if is_player:
        player.health = goal
    else:
        enemy.health = goal
    delta = is_add
    
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                terminate()
        Game(battle_bg)
        DrawCards(3)
        #判断哪一方受伤
        if is_add == -1:
            if is_player :
                DrawPlayer(player_im)
                DrawImage(enemy_im,game_Surface,100,100,left,100)
                DrawNum(2)
            else :
                DrawEnemy(enemy_im)
                DrawImage(player_im,game_Surface,100,100,left,100)
                DrawNum(10)
        if is_add == 1:
            if not is_player :
                DrawPlayer(player_im)
                DrawImage(enemy_im,game_Surface,100,100,left,100)
                DrawNum(10)
            else :
                DrawEnemy(enemy_im)
                DrawImage(player_im,game_Surface,100,100,left,100)
                DrawNum(2)
        
        if is_add == -1:
            DrawText('-%s'%(del_num),RED,small_Font,game_Surface,pos_x,pos_y+15)
        else:
            DrawText('+%s'%(del_num),RED,small_Font,game_Surface,pos_x,pos_y+15)
            DrawSurface(game_Surface)
        
        if (is_add == 1 and num < goal) or (is_add == -1 and num > goal):
            num += delta
            DrawText('%s'%(num),RED,small_Font,game_Surface,pos_x,pos_y)
            DrawSurface(game_Surface)
        
        if num == goal:
            return
        mainClock.tick(30)
def RaiseCards():
    del_y = 0
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                terminate()
        DrawBackground(battle_bg, game_Surface)#显示背景图
        DrawImage('bar.png',game_Surface,WINDOWWIDTH,50,0,0)
        DrawImage('energy.png',game_Surface,30,30,0,50)
        DrawText('Score  %s'%(score),WHITE,small_Font,game_Surface,30,90)
        DrawText('Lv.   %s'%(player.level),WHITE,small_Font,game_Surface,25,40)
        DrawImage('attack.png', game_Surface, Info_Key_Size+10, Info_Key_Size+10, 5, -5)
        DrawImage('health.png', game_Surface, Info_Key_Size, Info_Key_Size, 60, 0)
        DrawImage('defense.png', game_Surface, Info_Key_Size-5, Info_Key_Size-5, 150, 0)
        DrawImage('coin.png', game_Surface, Info_Key_Size, Info_Key_Size, 210, -3)

        DrawImage('血量.png',game_Surface,Info_Key_Size+3,Info_Key_Size+3, 260, -10)
        DrawImage('能量.png',game_Surface,Info_Key_Size,Info_Key_Size, 310, 0)
        DrawImage('爆炸.png',game_Surface,Info_Key_Size+5,Info_Key_Size+5, 370,-5)
        DrawImage('烟雾.png',game_Surface,Info_Key_Size,Info_Key_Size, 420, -2)
        
        DrawImage('health.png', game_Surface, Info_Key_Size, Info_Key_Size, 500, 0)
        DrawText('%s'%(player.attack),RED,small_Font,game_Surface,45,13)
        DrawText('%s'%(player.health),RED,small_Font,game_Surface,100,13)
        DrawText('/%s'%(player.max_health),RED,small_Font,game_Surface,130,13)
        DrawText('%s'%(player.defense),AZURE,small_Font,game_Surface,190,13)
        DrawText('%s'%(player.coin),GOLD,small_Font,game_Surface,250,13)
        DrawText('%s'%(player.itemsnum_1),RED,small_Font,game_Surface,300,13)
        DrawText('%s'%(player.itemsnum_2),RED,small_Font,game_Surface,350,13)
        DrawText('%s'%(player.itemsnum_3),RED,small_Font,game_Surface,410,13)
        DrawText('%s'%(player.itemsnum_4),RED,small_Font,game_Surface,450,13)
        DrawText('%s'%(enemy.health),RED,small_Font,game_Surface,550,13)
        DrawText('/%s'%(enemy.max_health),RED,small_Font,game_Surface,580,13)
        DrawText('%s'%(player.energy),AZURE,small_Font,game_Surface,40,63)
        DrawImage(enemy.image,game_Surface, 100, 100, 500 , 100)
        DrawImage(player.image,game_Surface, 100, 100,100,100)
        del_y += 5
        for i in range(3):
            DrawImage(card_names[i], game_Surface, CARDWIDTH, CARDHEIGHT, 
            110+150*i, WINDOWHEIGHT - del_y)
        DrawSurface(game_Surface)
        if del_y >= CARDHEIGHT*2/3:
            return
        mainClock.tick(FPS)
def Battle(battle_bg,player_im,enemy_im):#整个的战斗过程
    ori_level = player.level
    ori_coin = player.coin
    DrawNum(0) #0表示全画
    DrawPlayer(player_im)
    DrawEnemy(enemy_im)
    DrawCards(3)#全画
    DrawSurface(game_Surface)
    flag = 0#为0表示攻击方是玩家，反之则是敌人
    rounds = 0#表示回合数，暂时不显示到屏幕上
    while True :
        for event in pygame.event.get():
            if event.type == QUIT :
                terminate()
            if event.type == MOUSEBUTTONUP and not flag:
                x,y = pygame.mouse.get_pos()
                for i in range(4):#嗑药
                    global score,floor
                    if Isin(x,y,drugs[i]):
                        if i==0 and player.itemsnum_1 > 0 and player.health<player.max_health:#血量药

                            #clickSound.play()
                            bloodSound.play()
                            delta = (int)(player.max_health*random.randint(20,30)/100)
                            Change_Health(battle_bg,player_im,enemy_im,100,100,13,player.health,delta,1,1)
                            #player.health += 10
                            player.itemsnum_1 -= 1
                            Game(battle_bg)
                            DrawNum(0) #0表示全画
                            DrawPlayer(player_im)
                            DrawEnemy(enemy_im)
                            DrawCards(3)#全画
                            DrawSurface(game_Surface)
                        if i==1 and player.itemsnum_2 > 0 :#能量药
                            energySound.play()
                            player.itemsnum_2 -= 1
                            player.energy += 20
                            Game(battle_bg)
                            DrawNum(0) #0表示全画
                            DrawPlayer(player_im)
                            DrawEnemy(enemy_im)
                            DrawCards(3)#全画
                            DrawSurface(game_Surface)
                            pass#先略去效果
                        if i==2 and player.itemsnum_3 > 0:#炸弹药
                            bombSound.play()
                            Change_Health(battle_bg,player_im,enemy_im,500,550,13,enemy.health,25,-1,0)
                            player.itemsnum_3 -= 1
                            Game(battle_bg)
                            DrawNum(0) #0表示全画
                            DrawPlayer(player_im)
                            DrawEnemy(enemy_im)
                            DrawCards(3)#全画
                            DrawSurface(game_Surface)
                            pass#先略去效果
                            
                        if i==3 and player.itemsnum_4 > 0 and floor != num_level -1:#烟雾药
                            clickSound.play()
                            player.itemsnum_4 -= 1
                            Game(battle_bg)
                            DrawNum(0) #0表示全画
                            DrawPlayer(player_im)
                            DrawEnemy(enemy_im)
                            DrawCards(3)#全画
                            DrawSurface(game_Surface)
                            
                            score -= level.getpoint(floor)
                            if floor != num_level -1:
                                DrawText('Vive la France!',WHITE,basicFont,game_Surface,320,180)
                                End(ori_level,ori_coin)
                            return#先略去效果

                for i in range(3) :#玩牌
                    if  Isin(x,y,cards[i]):
                        if i==0 or i==1:
                            cardSound.play()
                            flag = 1
                            rounds+=1
                            temp = fa.cope(i+1,player,enemy)
                            if temp <= 0 :
                                temp = 1
                            Move_player(battle_bg,player_im,enemy_im,temp)
                        
                        if i==2 :
                            if player.energy>=100:
                                cardSound.play()
                                flag = 1
                                rounds+=1
                                temp = fa.cope(i+2,player,enemy)
                                if temp <= 0 :
                                    temp = random.randint(10,50)
                                #player.energy -= 100
                                
                                #if player.blessing_2 == 1:
                                    #player.health -= 5
                                    #Change_Health(battle_bg,player_im,enemy_im,100,100,13,player.health,5,-1,1)
                                Move_player(battle_bg,player_im,enemy_im,temp)
                            else:
                                DrawText('%s'%(player.energy),RED,small_Font,game_Surface,40,63)
                                time.sleep(0.2)
                                #DrawText('%s'%(player.energy),AZURE,small_Font,game_Surface,40,63)
                    #pass#使用攻击技能
        
        
        #结束以后跳转
        if enemy.health == 0:
            #预计是打上'press any key to continue'再进行跳转
            #结算 重新显示
            player.xp += enemy.xp
            player.coin += enemy.coin
            while player.xp>=xp_level[player.level]:
                    #print('your level has promted')
                    player.max_health=player.max_health+5
                    player.health=player.health+5
                    player.attack=player.attack+3
                    player.defense=player.defense+1
                    player.xp=player.xp-xp_level[player.level]
                    player.level=player.level+1
            if floor != num_level -1:
                End(ori_level,ori_coin)
            #time.sleep(0.5)
            return
        if player.health == 0:
            pygame.mixer_music.stop()
            time.sleep(0.2)
            DefeatSound.play()
            Font2 = pygame.font.SysFont('inkfree', 30)
            DrawText('Game Over!',WHITE,basicFont,game_Surface,200,200)
            DrawText('Press any key to continue...',WHITE,Font2,game_Surface,320,30)
            DrawSurface(game_Surface)
            while True:
                for event in pygame.event.get():
                    if event.type == KEYDOWN:
                        DefeatSound.stop()
                        return
                    if event.type == QUIT:
                        terminate()
        if flag :
            flag = 0
            enemy.attack *= (1+random.randint(2,4)/100*floor)
            if enemy.name=='ghost':
               enemy.health=enemy.max_health
            temp = fa.copeb(rounds,player,enemy)
            temp = (int)(temp)
            if temp <= 0 :
                temp = 1
            Move_enemy(battle_bg,player_im,enemy_im,temp)
        #创造点击效果
        x,y = pygame.mouse.get_pos()
        for i in range(3) :
           
            if Isin(x,y,cards[i]) and cards[i].top == WINDOWHEIGHT - CARDHEIGHT*2/3:
                cards[i].move_ip(0, -10)
                Game(battle_bg)
                DrawCards(i)
                DrawNum(0)
                DrawPlayer(player_im)
                DrawEnemy(enemy_im)
                DrawImage(card_names[i],game_Surface,CARDWIDTH,CARDHEIGHT,cards[i].left,cards[i].top)
            if not Isin(x,y,cards[i]) and cards[i].top < WINDOWHEIGHT - CARDHEIGHT*2/3:
                cards[i].move_ip(0, 10)
                Game(battle_bg)#刷新游戏界面
                DrawCards(i)
                DrawNum(0)
                DrawPlayer(player_im)
                DrawEnemy(enemy_im)
                DrawImage(card_names[i],game_Surface,CARDWIDTH,CARDHEIGHT,cards[i].left,cards[i].top)
        

        DrawSurface(game_Surface)
        mainClock.tick(FPS)
def End(ori_level,ori_coin):
    Font1 = pygame.font.SysFont('inkfree', 35)
    Next_Rect = DrawImage('next.png',game_Surface,220,50,460,-10)
    print(player.level)
    if player.level>ori_level:
        #DrawImage('buttonShadow.png',game_Surface,256,256,192,52)
        DrawText('Lv   %s'%(player.level)+'(+%s)'%(player.level-ori_level),
        WHITE,Font1,game_Surface,320,150)
        DrawText('Coin %s'%(player.coin)+'(+%s)'%(player.coin-ori_coin),
        GOLD,Font1,game_Surface,320,210)
    DrawSurface(game_Surface)
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                terminate()
            if event.type == MOUSEBUTTONUP:
                pos_x,pos_y = pygame.mouse.get_pos()
                if Isin(pos_x,pos_y,Next_Rect):
                    clickSound.play()
                    return
#商店事件
price = [0,0,0,0,0,0,0]
nums  = []
goods_button = []
def DrawNum2():
    DrawText('%s'%(player.coin),GOLD,small_Font,store_Surface,250,13)
    DrawText('%s'%(player.itemsnum_1),RED,small_Font,store_Surface,300,13)
    DrawText('%s'%(player.itemsnum_2),RED,small_Font,store_Surface,350,13)
    DrawText('%s'%(player.itemsnum_3),RED,small_Font,store_Surface,410,13)
    DrawText('%s'%(player.itemsnum_4),RED,small_Font,store_Surface,450,13)
def DrawGoods_Info(price,pos_x,pos_y):
    DrawText('num:',WHITE,small_Font,store_Surface,pos_x+25,pos_y+40)
    DrawImage('coin.png',store_Surface, Info_Key_Size, Info_Key_Size, pos_x, pos_y+45)
    DrawText('%s'%(price),GOLD,small_Font,store_Surface,pos_x+35,pos_y+60)
def DrawNums(goods_num,pos_x,pos_y):
    DrawText('%s'%(goods_num),WHITE,small_Font,store_Surface,pos_x,pos_y)
def Store():#加载商店界面
    
    pygame.display.set_caption('Store')
    DrawBackground('store.png',store_Surface)
    DrawImage('bar.png',store_Surface,WINDOWWIDTH,50,0,0)
    DrawNum2()
    Info_Key_Size2 = Info_Key_Size + 10
    DrawImage('coin.png',store_Surface, Info_Key_Size, Info_Key_Size, 210, -3)
    DrawImage('血量.png',store_Surface,Info_Key_Size+3,Info_Key_Size+3, 260, -10)
    DrawImage('能量.png',store_Surface,Info_Key_Size,Info_Key_Size, 310, 0)
    DrawImage('爆炸.png',store_Surface,Info_Key_Size+5,Info_Key_Size+5, 370,-5)
    DrawImage('烟雾.png',store_Surface,Info_Key_Size,Info_Key_Size, 420, -2)
    DrawImage('shop.png',store_Surface,220,50,-50,-10)
    Next_Rect = DrawImage('next.png',store_Surface,220,50,460,-10)

   
    
    #goodsnames = ['burningBlood.png','attackBuff.png','duality.png','血量.png','能量.png','爆炸.png','烟雾.png']

    x = [410,300,530,300,380,460,540]
    y = [ 100,120,120,230,230,230,230]
    #siz = [100,60,60,60,50,60,50]
    for i in range(7):
        DrawGoods_Info(price[i],x[i],y[i])

    #---画商品
    
    goods_rect = DrawImage('burningBlood.png',store_Surface,100,100,390,60)
    goods_button.append(goods_rect)
    goods_rect = DrawImage('attackBuff.png',store_Surface,60,60,300,95)
    goods_button.append(goods_rect)
    goods_rect = DrawImage('duality.png',store_Surface,80,80,515,90)
    goods_button.append(goods_rect)
    goods_rect = DrawImage('血量.png',store_Surface,50,50,300,210)
    goods_button.append(goods_rect)
    goods_rect = DrawImage('能量.png',store_Surface,50,50,380,220)
    goods_button.append(goods_rect)
    goods_rect = DrawImage('爆炸.png',store_Surface,60,60,460,215)
    goods_button.append(goods_rect)
    goods_rect = DrawImage('烟雾.png',store_Surface,50,50,540,220)
    goods_button.append(goods_rect)
    

    DrawSurface(store_Surface)
def Change(x):
    if x == 0 :
        player.max_health += 10
    if x==1:
        player.attack += 10
    if x == 2:
        player.defense += 3
    if x==3 :
        player.itemsnum_1 += 1
    if x==4 :
        player.itemsnum_2 += 1
    if x==5 :
        player.itemsnum_3 += 1
    if x==6 :
        player.itemsnum_4 += 1
def Load():
    left = 0
    right = 0
    moverate = 5
    startSound.play()
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                terminate()
        DrawBackground('store.png',store_Surface)
        DrawImage('bar.png',store_Surface,WINDOWWIDTH,50,0,0)
        DrawNum2()
        Info_Key_Size2 = Info_Key_Size + 10
        DrawImage('coin.png',store_Surface, Info_Key_Size, Info_Key_Size, 210, -3)
        DrawImage('血量.png',store_Surface,Info_Key_Size+3,Info_Key_Size+3, 260, -10)
        DrawImage('能量.png',store_Surface,Info_Key_Size,Info_Key_Size, 310, 0)
        DrawImage('爆炸.png',store_Surface,Info_Key_Size+5,Info_Key_Size+5, 370,-5)
        DrawImage('烟雾.png',store_Surface,Info_Key_Size,Info_Key_Size, 420, -2)
        DrawImage('shop.png',store_Surface,220,50,-50,-10)
        DrawImage('next.png',store_Surface,220,50,460,-10)
        x = [410,300,530,300,380,460,540]
        y = [ 100,120,120,230,230,230,230]
        for i in range(7):
            DrawGoods_Info(price[i],x[i],y[i])
        x1 = [455,350,580,350,430,510,590]
        y1 = [140,160,160,270,270,270,270]
        for i in range(7):
            DrawNums(nums[i],x1[i],y1[i])
    #---画商品
        
        DrawImage('burningBlood.png',store_Surface,100,100,390,60)
        DrawImage('attackBuff.png',store_Surface,60,60,300,95)
        DrawImage('duality.png',store_Surface,80,80,515,90)
        DrawImage('血量.png',store_Surface,50,50,300,210)
        DrawImage('能量.png',store_Surface,50,50,380,220)
        DrawImage('爆炸.png',store_Surface,60,60,460,215)
        DrawImage('烟雾.png',store_Surface,50,50,540,220)
        DrawImage('door_left.png',store_Surface,WINDOWWIDTH,WINDOWHEIGHT,left ,0)
        DrawImage('door_right.png',store_Surface,WINDOWWIDTH,WINDOWHEIGHT,right ,0)
        left -= moverate
        right += moverate
        DrawSurface(store_Surface)
        #time.sleep(0.1)
        if left <= -300 and right>=300:
            return
        mainClock.tick(FPS)
def Purchase():
    Next_Rect = DrawImage('next.png',store_Surface,220,50,460,-10)
    x = [455,350,580,350,430,510,590]
    y = [140,160,160,270,270,270,270]
    for i in range(7):
        DrawNums(nums[i],x[i],y[i])
    DrawSurface(store_Surface)
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                terminate()
            if event.type == MOUSEBUTTONUP:
                pos_x,pos_y = pygame.mouse.get_pos()
                for i in range(7):
                    if Isin(pos_x,pos_y,goods_button[i]):
                        
                        if player.coin < price[i]:
                            
                            DrawText('%s'%(player.coin),RED,small_Font,store_Surface,250,13)
                            DrawSurface(store_Surface)
                            time.sleep(0.5)
                        else:
                            if nums[i]==0:
                                DrawText('%s'%(nums[i]),RED,small_Font,store_Surface,x[i],y[i])
                                DrawSurface(store_Surface)
                                time.sleep(0.5)
                            else :
                                clickSound.play()
                                time.sleep(0.2)
                                if i==0:#加血
                                    bloodSound.play()
                                if i==1:
                                    attackSound.play()
                                if i==2:
                                    defenseSound.play()
                                buySound.play()
                                nums[i] -=1
                                Change(i)
                                player.coin -= price[i]
                    Store()
                    DrawNum2()
                    for j in range(7):
                        DrawNums(nums[j],x[j],y[j])
                    DrawSurface(store_Surface)

                if Isin(pos_x,pos_y,Next_Rect):
                    clickSound.play()
                    return

        mainClock.tick(FPS)


Event_bg = ['event_1.png','event_2.png']
event1_surface =  pygame.Surface(windowSurface.get_size())
def Next_():
    Next_Rect = DrawImage('next.png',event_surface,220,50,460,-10)
    DrawSurface(event_surface)
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                terminate()
            if event.type == MOUSEBUTTONUP:
                pos_x,pos_y = pygame.mouse.get_pos()
                if Isin(pos_x,pos_y,Next_Rect):
                    clickSound.play()
                    return
def Motion_1(card_im,x):
    y = 105
    DrawImage(card_names[2],event_surface,CARDWIDTH,CARDHEIGHT,265,y)
    DrawSurface(event_surface)
    time.sleep(0.5)
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                terminate()
        DrawBackground(Event_bg[x],event_surface)
        DrawImage('panel.png',event1_surface,340,30,265,280)
        DrawImage('panel.png',event1_surface,340,30,265,315)

        DrawImage(card_names[2],event_surface,CARDWIDTH,CARDHEIGHT,265,y)
        DrawSurface(event_surface)
        if y + CARDHEIGHT <=0 :
            break
        y -= 10
        mainClock.tick(FPS)
    y = WINDOWHEIGHT
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                terminate()
        DrawBackground(Event_bg[x],event_surface)
        DrawImage('panel.png',event1_surface,340,30,265,280)
        DrawImage('panel.png',event1_surface,340,30,265,315)

        DrawImage(card_im,event_surface,CARDWIDTH,CARDHEIGHT,265,y)
        DrawSurface(event_surface)
        if y <=105 :
            break
        y -= 10
        mainClock.tick(FPS)
def Motion_2(opt,x,ori):
    if opt == 0:
        attackSound.play()
        im = 'attack.png'
        num = 5
    else:
        bloodSound.play()
        im = 'health.png'
        num = 7
    Font2 = pygame.font.SysFont('inkfree', 25)
    DrawBackground(Event_bg[x],event_surface)
    if opt == 1:
        DrawText('Max',RED,Font2,event_surface,305,220)
    DrawImage(im,event_surface,50,50,320,200)
    DrawText('%s'%(ori),RED,Font2,event_surface,425,217)
    while True:
        for event in pygame.event.get():
            if event.type == QUIT :
                terminate()
        DrawBackground(Event_bg[x],event_surface)
        if opt == 1:
            DrawText('Max',RED,Font2,event_surface,305,220)
        DrawImage(im,event_surface,50,50,320,200)
        ori += 1
        DrawText('  %s'%(ori)+' (+%s)'%(num),RED,Font2,event_surface,425,217)
        DrawSurface(event_surface)
        if (opt == 0 and ori-player.attack == num) or (opt == 1 and ori-player.max_health == num):
            return
        mainClock.tick(10)
        
flag = 0
def Event_(x):#事件界面
    global flag
    if not flag:
        eventSound.play()
        flag = 1
    DrawBackground(Event_bg[x],event_surface)
    opt_1 = DrawImage('panel.png',event1_surface,340,30,265,280)
    opt_2 = DrawImage('panel.png',event1_surface,340,30,265,315)
    DrawSurface(event_surface)

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                terminate()
            if event.type == MOUSEBUTTONUP:
                pos_x,pos_y = pygame.mouse.get_pos()
                if x==0:
                    clickSound.play()
                    if Isin(pos_x,pos_y,opt_1):
                        player.blessing_1 =1
                        player.blessing_2 =0

                        Motion_1('card5.png',x)
                        card_names[2] = 'card5.png'
                        Next_()
                        return
                    if Isin(pos_x,pos_y,opt_2):
                        player.blessing_2 =1 
                        player.blessing_1 =0

                        Motion_1('card4.png',x)
                        card_names[2] = 'card4.png'
                        Next_()
                        return
                if x==1:
                    clickSound.play()
                    if Isin(pos_x,pos_y,opt_1):
                        Motion_2(0,x,player.attack)
                        player.attack += 5
                        Next_()
                        return
                    if Isin(pos_x,pos_y,opt_2):
                        Motion_2(1,x,player.max_health)
                        player.max_health += 7
                        Next_()
                        return



#初始化变量
floor = 0#表示第几关
playing=0
score = 0
total_score=0
game_times=0#游戏次数
highest_score=0
finsh_times=0#游戏成功次数
score=0
if os.path.isfile('全局数据.txt'):#这是检查有无这个文件如果是第一次开没有文件就不读以免报错
    total_score,game_times,highest_score,finsh_times,playing=saveload.read1(total_score,game_times,highest_score,finsh_times,playing)
xp_level=[5,15,20,25,60,100,200,99999]#这是等级所需经验
#enemy.image = 'baddie1.png'
#enemy.name = 'bird'

#i=0#目前在进行第几关
#map=[1,2,0,0,0,0,0,0]
#vis=[0,0,0,0,0,0,0,0]#这是用于生成地图时检索是否被生成过以达到遍历的目的
num_level=9#地图里有多少关
#地图数组生成
#退出标识
flag_exit=0
while True:
    #初始化
    
    me=my_class.Mob(100,20,3,0,0)
    me.image='player.png'
    me.coin=30
    me.xp=0
    me.level=1
    me.itemsnum_1=2#生血药
    me.itemsnum_2=1#能量药
    me.itemsnum_3=0#爆炸弹（给敌人造成20点伤害）
    me.itemsnum_4=0#烟雾弹
    me.itemsnum=0#道具总量（背包总量）
    me.blessing_1=0
    me.blessing_2=0
    if playing==1:
        me=saveload.read2(me)
        if me.blessing_1 :
            card_names[2] = 'card5.png'
        if me.blessing_2:
            card_names[2] = 'card4.png'
    score = 0
    player = me
    battle_bg = 'battle_1.jpg'

    pygame.mixer.music.load('背景音乐.ogg')
    pygame.mixer.music.play(-1,0,0)
    Background('start.png')
    pygame.mixer.music.stop()

    i=0
    map = fa.summonmap()
    bg = ['battle_1.jpg','battle_2.jpg','battle_3.jpg','battle_4.png','battle_5.jpg']
    if playing==1:
        num_level,map,i,score=saveload.read3(num_level,map,i,score)
        
    while i<num_level:
        floor = i
        vis = [0,0]
        playing=1
        x = level.gettype(map[i])
        saveload.write1(total_score,game_times,highest_score,finsh_times,playing)
        saveload.write2(me)#主角的所有属性    
        if x==1:
            enemy = level.got(map[i],player)
            enemy.health = enemy.max_health
            player1 = player#记录战斗开始前player的数据
            tt = random.randint(0,4)
            battle_bg = bg[tt]
            pygame.mixer.music.load('事件音乐.ogg')
            pygame.mixer.music.play(-1,0,0)
            RaiseCards()
            Game(battle_bg)
            Battle(battle_bg,player.image,enemy.image)
            pygame.mixer.music.stop()
            if player.health == 0:
                playing = 0
                break
            if i==num_level - 1:
                VictorySound.play()
                Font2 = pygame.font.SysFont('inkfree', 30)
                score=score+level.getpoint(map[i])
                DrawText('You Win',GOLD,basicFont,game_Surface,200,200)
                DrawText('Total Score: %s'%(score),GOLD,Font2,game_Surface,200,240)
                if score > highest_score:
                        DrawText('(New record!)',GOLD,Font2,game_Surface,200,270)
                DrawText('Press any key to continue...',WHITE,Font2,game_Surface,320,30)
                DrawSurface(game_Surface)
                while True:
                    temp = 0
                    for event in pygame.event.get():
                        if event.type == QUIT:
                            terminate()
                        if event.type == KEYDOWN:
                            VictorySound.stop()
                            temp = 1
                            break
                    if temp:
                        playing = 0
                        break
        if x==2:
            
            flag = 0#表示要不要放开始的音乐（0表示放）
            '''pygame.mixer.music.load('事件音乐.ogg')
            pygame.mixer.music.play()'''
            t = random.randint(0,1)
            if not vis[t]:
                Event_(t)
                vis[t] = 1
            else:
                Event_(1-t)
                vis[t] = 1
            #pygame.mixer.music.stop()
        if x==3:
            for j in range(7):
                nums.append(random.randint(2,5))
            price[0] = price[1]= 10
            price[2] = 20
            price[3]=price[4] = 10
            price[5] = 20
            price[6] = 30
            for j in range(7):
                price[j] += random.randint(-3,10)
            if floor > 3:
                for j in range(7):
                    price[j] += random.randint(20,30)

            Load()
            Store()
            Purchase()
        score=score+level.getpoint(map[i])
        i=i+1
        saveload.write3(num_level,map,i,score)
    
    if i==num_level :
        print('you finished')
        finsh_times += 1
        playing = 0
        i = 0
        if score > highest_score :
            highest_score = score
        saveload.write1(total_score,game_times,highest_score,finsh_times,playing)
        saveload.write2(me)
        saveload.write3(num_level,map,i,score)
