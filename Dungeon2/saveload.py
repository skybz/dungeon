#全局读档（总积分）
def read1(total_score,game_times,highest_score,finsh_times,playing):
    file1=open('全局数据.txt','r')
    total_score=int(file1.readline())
    game_times=int(file1.readline())
    highest_score=int(file1.readline())
    finsh_times=int(file1.readline())
    playing=int(file1.readline())
    file1.close()
    return total_score,game_times,highest_score,finsh_times,playing

def write1(total_score,game_times,highest_score,finsh_times,playing):#全局存档（总积分）
    file1=open("全局数据.txt","w")
    file1.write(str(total_score))
    file1.write("\n")
    file1.write(str(game_times))
    file1.write("\n")
    file1.write(str(highest_score))
    file1.write("\n")
    file1.write(str(finsh_times))
    file1.write("\n")
    file1.write(str(playing))
    file1.write("\n")
    file1.close()

def read2(a):#主角读档
    file1=open("主角数据.txt","r")
    a.max_health=int(file1.readline())
    a.health=int(file1.readline())
    a.energy=int(file1.readline())
    a.attack=int(file1.readline())
    a.defense=int(file1.readline())
    a.itemsnum_1=int(file1.readline())
    a.itemsnum_2=int(file1.readline())
    a.itemsnum_3=int(file1.readline())
    a.itemsnum_4=int(file1.readline())
    a.blessing_1=int(file1.readline())
    a.blessing_2=int(file1.readline())
    a.level=int(file1.readline())
    file1.close()
    return a

def write2(a):#主角存档
    file1=open("主角数据.txt","w")
    file1.write(str(a.max_health))
    file1.write("\n")
    file1.write(str(a.health))
    file1.write("\n")
    file1.write(str(a.energy))
    file1.write("\n")
    file1.write(str(a.attack))
    file1.write("\n")
    file1.write(str(a.defense))
    file1.write("\n")
    file1.write(str(a.itemsnum_1))
    file1.write("\n")
    file1.write(str(a.itemsnum_2))
    file1.write("\n")
    file1.write(str(a.itemsnum_3))
    file1.write("\n")
    file1.write(str(a.itemsnum_4))
    file1.write("\n")
    file1.write(str(a.blessing_1))
    file1.write("\n")
    file1.write(str(a.blessing_2))
    file1.write("\n")
    file1.write(str(a.level))
    file1.write("\n")
    file1.close()

def read3(num_level,map,i,score):#关卡读档
    file1=open("关卡.txt","r+")
    num_level=int(file1.readline())#n 总关卡数
    #playing=int(file1.readline())#用0，1表示有没有玩过
    temp=0
    while temp<num_level:
        map[temp]=int(file1.readline())
        temp=temp+1
    i=int(file1.readline())#i 目前第几关
    score=int(file1.readline())
    return num_level,map,i,score
    file1.close()

def write3(num_level,map,i,score):#关卡存档
    file1=open("关卡.txt","w")
    #n=4
    #playing=1 玩过没有
    #Map=[0,1,2,3,4]
    #i=2  目前处在第几关
    file1.write(str(num_level))
    file1.write("\n")
    temp=0
    while temp<num_level:
        file1.write(str(map[temp]))
        file1.write("\n")
        temp=temp+1
    file1.write(str(i))
    file1.write("\n")
    file1.write(str(score))
    file1.write("\n")
    file1.close()







    
