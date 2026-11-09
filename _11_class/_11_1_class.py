class Ork:
    def __init__(self, level):
        self.level = level
        self.health = 100 * level
        self.attack_power = 4 * level

    def attack(self):
       print( f"Атака орка {self.attack_power}")

    def __str__(self):
        return f"Орк(Уровень {self.level}. Хп {self.health})"




class Elf:
    def __init__(self, level):
        self.level = level
        self.health = 50 * level
        self.attack_power = 6 * level

    def attack(self):
       print( f"Атака эльфа {self.attack_power}")

    def __str__(self):
           return f"Эльф(Уровень {self.level}. Хп {self.health})"