from robot import Robot

class Fleet:
    def __init__(self):
        self.robots = []
        self.create_fleet()


    def create_fleet(self):
        robot_one = Robot("Bumblebee", 100,"sword", 10)
        robot_two = Robot("Starscream", 100, "flamethrower", 15) 
        robot_three = Robot("Optimus Prime", 100, "laser", 20)

        self.robots.append(robot_one)
        self.robots.append(robot_two)
        self.robots.append(robot_three) 