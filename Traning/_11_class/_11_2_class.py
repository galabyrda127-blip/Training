class Character:
    # --- Значения по умолчанию (заглушки). Настоящие задают подклассы Ork и Elf ---
    base_health = 0        # здоровье за 1 уровень
    base_attack = 0        # сила атаки за 1 уровень
    character_name = ""    # имя персонажа
    base_defence = 0       # защита (в %) за 1 уровень
    max_level = 3          # максимальный уровень, выше не поднимется

    # --- Повышение уровня ---
    def level_up(self):
        # Если уровень уже максимальный, ничего не делаем
        if self.level >= self.max_level:
            return
        self.level += 1
        # Атака хранится готовым числом, поэтому после повышения пересчитываем её
        self.attack_power = self.base_attack * self.level
        # Отхил: прибавляем половину максимального хп (уже по новому уровню)
        self.health_points += self.max_health // 2

    # --- Создание персонажа ---
    def __init__(self, *, level):
        self.level = level
        # Здоровье и атака = базовое значение * уровень
        self.health_points = self.base_health * level
        self.attack_power = self.base_attack * level

    # --- Получение урона ---
    def got_damage(self, damage):
        # Защита уменьшает урон в процентах: защита 20% -> проходит 80% урона
        damage = damage * (100 - self.defence) / 100
        damage = round(damage)               # округляем до целого
        self.health_points -= damage         # отнимаем от здоровья

    # --- Атака ---
    def attack(self, *, target: "Character"):
        # Атакующий (self) наносит цели (target) урон, равный своей силе атаки
        target.got_damage(damage=self.attack_power)

    # --- Проверка: жив ли ---
    def is_alive(self):
        return self.health_points > 0        # True, если хп больше нуля

    # --- Защита (@property: вызывается без скобок, считается заново каждый раз) ---
    @property
    def defence(self):
        # Не больше 90%, иначе урон начнёт лечить
        return min(self.base_defence * self.level, 90)

    # --- Максимальное здоровье (считается по уровню, а не по текущему хп) ---
    @property
    def max_health(self):
        return self.level * self.base_health

    # --- Сколько процентов здоровья осталось ---
    def health_procent(self):
        return self.health_points / self.max_health * 100

    # --- Как персонаж выглядит при print ---
    def __str__(self):
        return f"{self.character_name}(Уровень {self.level}. Хп {self.health_points})"


# ===================== Подклассы =====================

class Ork(Character):
    # Свои цифры орка
    base_health = 100
    base_attack = 4
    character_name = "Ork"
    base_defence = 15

    # Особенность орка: при хп меньше 50 защита утраивается
    @property
    def defence(self):
        defence = super().defence            # обычная защита из родителя
        if self.health_points < 50:
            defence = min(defence * 3, 90)   # утроили, но не больше 90
        return defence


class Elf(Character):
    # Свои цифры эльфа
    base_health = 50
    base_attack = 6
    character_name = "Elf"
    base_defence = 10

    # Особенность эльфа: добивает слабых, урон x3 если у цели меньше 30% хп
    def attack(self, *, target: "Character"):
        attack_power = self.attack_power
        if target.health_procent() < 30:
            attack_power = self.attack_power * 3
        target.got_damage(damage=attack_power)


# ===================== Бой =====================

def fight(*, ch_1, ch_2):
    # Бой идёт, пока оба живы
    while ch_1.is_alive() and ch_2.is_alive():
        ch_1.attack(target=ch_2)             # первый бьёт второго
        if not ch_2.is_alive():              # второй умер
            ch_1.level_up()                  # победитель получает уровень
            break                            # мёртвый не бьёт в ответ
        ch_2.attack(target=ch_1)             # второй бьёт в ответ
        if not ch_1.is_alive():              # первый умер
            ch_2.level_up()                  # победитель получает уровень

    # Итог боя: имя, жив или мёртв, и данные персонажа
    for ch in (ch_1, ch_2):
        status = "alive" if ch.is_alive() else "dead"
        print(f"{ch.character_name} is {status} {ch}")


# ===================== Запуск =====================

ork_1 = Ork(level=1)
elf_1 = Elf(level=2)
print(ork_1, elf_1, end=2 * "\n")            # персонажи до боя, потом пустая строка

fight(ch_1=ork_1, ch_2=elf_1)