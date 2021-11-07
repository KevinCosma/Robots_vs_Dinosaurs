from weapon import Weapon 


class Robot:
    def __init__(self, robot_name, robot_health, weapon_name, weapon_power):
        self.name = robot_name
        self.health = robot_health
        self.weapon = Weapon(weapon_name, weapon_power)

    def attack(self, dinosaur):
       dinosaur.health = dinosaur.health - self.weapon
        

