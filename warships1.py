import random

#print(random.randint(1,101))

def ranpc():
    return random.randint(1,100)

def rantt():
    return random.randint(1,10000)

class Battleship:
    
    def __init__(self,name):
        self.health = 120
        self.firepower = 50
        self.firecontrol = 50
        self.armour = 50
        self.name = name
    
    def shoot_at(self,target):
        if self.firecontrol > ranpc():
            print(target.name,"hit!")
            target.is_hit(self.firepower)
        else:
            print(self.name,"missed")
        pass        
    
    def is_hit(self,firepower):
        damage = firepower / self.armour * ranpc()
        self.health = self.health - damage
        if self.is_sunk():
            print(self.name,"sunk!")
    
    def is_sunk(self):
        if self.health < 0:
            return True
        else:
            return False

    def is_afloat(self):
        return not self.is_sunk()
        
#print(ranpc())
#print(random.randint(1,100))

w1 = Battleship("BISMARK")
w2 = Battleship("HOOD")

ships = [w1,w2]


#print("w2 is afloat is",w2.is_afloat())


while w2.is_afloat() and w1.is_afloat():
    action = int(input("""
Select action:
  1. HOOD shoots at BISMARK
  2. BISMARK shoots at HOOD
  """))
  
    if action == 2:
        w1.shoot_at(w2)
    else:
        w2.shoot_at(w1)
    #print("w2 is afloat is",w2.is_afloat())


#print("w1 health is ",w1.health,"w2 health is",w2.health)