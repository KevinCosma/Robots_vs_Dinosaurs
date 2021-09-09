from dinosaur import Dinosaur

class Herd:
    def __init__(self):
        self.dinosaurs = []

    def herd(self):
        dinosaur_one = Dinosaur('Stegasaurous')
        dinosaur_two = Dinosaur("Triceratops")
        dinosaur_three = Dinosaur("Tyranasaurous")

        self.dinosaurs.append(dinosaur_one)
        self.dinosaurs.append(dinosaur_two)
        self.dinosaurs.append(dinosaur_three)