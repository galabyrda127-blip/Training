class Character:
    base_health = 0
    base_attack = 0
    character_name = ""
    base_defence = 0

    def __init__(self,*, level):
        self.level = level
        self.health_points = self.base_health * level
        self.attack_power = self.base_attack * level

    def got_damage(self, damage):
        damage = damage * (100 - self.defence) /100
        damage = round (damage)
        self.health_points -=  damage


    def attack(self,*,target: "Character"):
        target.got_damage(damage=self.attack_power)

    def is_alive(self):
        return  self.health_points > 0

    @property
    def defence(self):
        defence =  self.base_defence * self.level
        return defence

    @property
    def max_health(self):
        return self.level * self. base_health


    def health_procent(self):
        return self.health_points / self.max_health * 100

    def __str__(self):
          return f"{self.character_name}(Уровень {self.level}. Хп {self.health_points})"


class Ork(Character):
    base_health = 100
    base_attack = 4
    character_name = "Ork"
    base_defence = 15

    @property
    def defence(self):
        defence = super().defence
        if self.health_points < 50:
            defence = defence * 3
        return defence



class Elf(Character):
    base_health = 50
    base_attack = 6
    character_name = "Elf"
    base_defence = 10

    def attack(self, *, target: "Character"):
        attack_power = self.attack_power
        if target.health_procent() < 30:
            attack_power = self.attack_power * 3
        target.got_damage(damage=attack_power)




def fight(*, ch_1, ch_2, ):
    while ch_1.is_alive() and ch_2.is_alive():
      ch_1.attack(target=ch_2)
      if  ch_2.is_alive():
          ch_2.attack(target=ch_1)

    print(f"Персонаж 1-{ch_1}, жив {ch_1.is_alive()}")
    print(f"Персонаж 2-{ch_2}, жив {ch_2.is_alive()}")

ork_1 = Ork(level=4)
elf_1 = Elf(level=6)

fight(ch_1=ork_1, ch_2=elf_1)

