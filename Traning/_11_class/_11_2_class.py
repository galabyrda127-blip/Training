class Character:
    base_health = 0
    base_attack = 0
    character_name = ""
    base_defence = 0
    max_level = 3

    def level_up(self):
        if self.level >= self.max_level:
            return
        self.level += 1
        self.attack_power = self.base_attack * self.level
        self.health_points += self.max_health // 2

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
        return min(self.base_defence * self.level, 90)

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
            defence = min(defence * 3, 90)
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




def fight(*, ch_1, ch_2):
    while ch_1.is_alive() and ch_2.is_alive():
        ch_1.attack(target=ch_2)
        if not ch_2.is_alive():
            ch_1.level_up()
            break
        ch_2.attack(target=ch_1)
        if not ch_1.is_alive():
            ch_2.level_up()

    for ch in (ch_1, ch_2):
        status = "alive" if ch.is_alive() else "dead"
        print(f"{ch.character_name} is {status} {ch}")



ork_1 = Ork(level=1)
elf_1 = Elf(level=2)

fight(ch_1=ork_1, ch_2=elf_1)

