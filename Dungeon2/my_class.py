class Mob(object):
 def __init__(self,max_health,attack,defense,crit_rate,energy):
    self.attack=attack
    self.max_health=max_health
    self.defense=defense
    self.crit_rate=crit_rate#造成额外伤害的数值
    self.health=max_health
    self.energy=energy
class Room(object):
 def __init__(self,type,point):
     self.type=type
     self.point=point
