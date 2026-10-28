class Character:
    base_health = 0
    base_attack = 0
    character_name = ""
    def __init__(self,*, level):
        self.level = level
        self.health_points = self.base_health * level
        self.attack_power = self.base_attack * level

    def attack(self,*,target: "Character"):
        print(
            f"{self.character_name} атакует {target.character_name}({target.health_points}хп)"
            f" сила атаки {self.attack_power}"
        )
        target.health_points -=self.attack_power
        print(f"Атакован  {target.character_name} осталось хп {target.health_points}", end = 2 * "\n")

    def is_alive(self):
        return self.health_points > 0

    def __str__(self):
          return f"{self.character_name}(Уровень {self.level}. Хп {self.health_points})"


class Ork(Character):
    base_health = 100
    base_attack = 4
    character_name = "Ork"



class Elf(Character):
    base_health = 50
    base_attack = 6
    character_name = "Elf"


def fight(*, ch_1, ch_2, ):
    while ch_1.is_alive() and ch_2.is_alive():
      ch_1.attack(target=ch_2)
      if  ch_2.is_alive():
          ch_2.attack(target=ch_1)

    print(f"Персонаж 1-{ch_1}, жив {ch_1.is_alive()}")
    print(f"Персонаж 2-{ch_2}, жив {ch_2.is_alive()}")

ork = Ork(level=10)
elf = Elf(level=11)

fight(ch_1=ork, ch_2=elf)