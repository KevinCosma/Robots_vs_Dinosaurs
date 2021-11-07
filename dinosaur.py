class Dinosaur:
    def __init__(self, dino_name, dino_attack_power, dino_health):
        self.name = dino_name
        self.attack_power = dino_attack_power
        self.health = dino_health
    
    def attack(self, robot):
        robot.health = robot.health - self.attack_power