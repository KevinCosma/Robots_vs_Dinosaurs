from dinosaur import Dinosaur

class Herd:
    def __init__(self):
        self.dinosaurs = []
        self.creat_herd()

    def creat_herd(self):
        dinosaur_one = Dinosaur('Stegasaurous', 10, 100)
        dinosaur_two = Dinosaur("Triceratops", 15, 100)
        dinosaur_three = Dinosaur("Tyranasaurous", 20, 100)

        self.dinosaurs.append(dinosaur_one)
        self.dinosaurs.append(dinosaur_two)
        self.dinosaurs.append(dinosaur_three)