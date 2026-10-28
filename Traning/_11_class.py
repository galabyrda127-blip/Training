class Character:
    def __init__(self,*, level):
        self.level = level
        self.health_points = self.base_health * level
        self.attack_power = self.base_attack * level

    def attack(self):
           print( f"Атака {self.character_name} -  {self.attack_power}", end = 2*"\n")

    def __str__(self):
          return f"{self.character_name}(Уровень {self.level}. Хп {self.health_points})"


class Ork(Character):
    base_health = 100
    base_attack = 4
    character_name = "Ork"

ork_1 = Ork(level=1)
print(ork_1)
ork_1.attack()


class Elf(Character):
    base_health = 50
    base_attack = 6
    character_name = "Elf"

elf_1 = Elf(level=1)
print(elf_1)
elf_1.attack()


# class Ork:
#     def __init__(self, level):
#         self.level = level
#         self.health = 100 * level
#         self.attack_power = 4 * level
#
#     def attack(self):
#        print( f"Атака орка {self.attack_power}")
#
#     def __str__(self):
#         return f"Орк(Уровень {self.level}. Хп {self.health})"
#
#
#
#
# class Elf:
#     def __init__(self, level):
#         self.level = level
#         self.health = 50 * level
#         self.attack_power = 6 * level
#
#     def attack(self):
#        print( f"Атака эльфа {self.attack_power}")
#
#     def __str__(self):
#            return f"Эльф(Уровень {self.level}. Хп {self.health})"