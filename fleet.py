from robot import Robot
from weapon import Weapon

class Fleet:
    def __init__(self):
        self.robots = []

    def fleet(self):
        robot_one = Robot("Bumblebee", 100), Weapon("sword", 10)
        robot_two = Robot("Starscream", 100), Weapon("flamethrower", 15) 
        robot_three = Robot("Optimus Prime"), Weapon("laser", 20)

        self.robots.append(robot_one)
        self.robots.append(robot_two)
        self.robots.append(robot_three) 