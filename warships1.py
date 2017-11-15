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
    
    def engage(self):
        input_string = "Select target\n"
        options = ships[:]
        options.remove(self)
        if len(options) == 1:
            target=options[0]
            print(target.name," selected as target")
        else:
           for i in range(len(options)):
               input_string = input_string +"\t" + str(i) + ". " + options[i].name + "\n"
           
           select = input(input_string)
           target = ships[int(select)]    
        #print("check point")
        distance = int(input("Enter range (in km):"))

        self.shoot_at(target,distance)
    
    def shoot_at(self,target,distance):
        if (self.firecontrol - distance) > ranpc():
            print("Hit!\n\n")
            target.is_hit(self.firepower)
        else:
            print("Missed\n\n")
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
active_ship_actions = ["Fire","Abandon ship","Retreat"]

#print("w2 is afloat is",w2.is_afloat())


while w2.is_afloat() and w1.is_afloat():
    input_string_1 = "Select ship\n"
    for i in range(len(ships)):
        input_string_1 = input_string_1 +"\t" + str(i) + ". " + ships[i].name + "\n"
    
    select_1 = input(input_string_1)
    active_ship = ships[int(select_1)]
    
    
    #print(active_ship.name)
    input_string_2 = "Select action\n"
    for i in range(len(active_ship_actions)):
        input_string_2 = input_string_2 +"\t" + str(i) + ". " + active_ship_actions[i] + "\n"
    
    select_2 = input(input_string_2)
    active_ship_action = active_ship_actions[int(select_2)]
    
    
    if active_ship_action == "Fire":
        active_ship.engage()



#print("w1 health is ",w1.health,"w2 health is",w2.health)