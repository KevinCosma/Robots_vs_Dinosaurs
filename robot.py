from weapon import Weapon 


class Robot:
    def __init__(self, Weapon):
        self.name = " "
        self.health = 0
        self.weapon = Weapon

    def robot(self):
        self.robot_one = ("Bumbelbee", 100, Weapon("sword"))
        self.robot_two = ("Starscream", 100, Weapon("laser"))
        self.robot_three = ("Optimus Prime", 100, Weapon("flamethrower"))
        

