from weapon import Weapon 

class Robot:
    def __init__(self, name, Weapon):
        self.name = " "
        self.health = 0
        self.weapon = Weapon

    def name(self):
        self.name_one = ("Bumbelbee", 100, Weapon("sword"))
        self.name_two = ("Starscream", 100, Weapon("laser"))
        self.name_three = ("Optimus Prime", 100, Weapon("flamethrower"))
        

