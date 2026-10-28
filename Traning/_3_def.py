import random

orel = "orel"
reshka = "reshka"
cn = [orel, reshka]

def flip():
    return random.choice(cn)

def martingale(*, depozit: int, min_bet: int, max_bet: int) -> tuple[int, int]:
    steps = 0
    #current_bet = min_bet
    max_depozit = depozit
    while depozit > 0:
       # current_bet = min(current_bet, depozit)
       # меняем min_bet -> current_bet если не хотим влезать в долги
        steps += 1
        depozit -= min_bet   #current_bet
        flipping_coin = flip()
        player_choice = flip()
        print(f"Игрок выбрал: {player_choice}")
        print("=====")
        print(f"Ставка: {min_bet}")  #current_bet
        print(f"Выпало: {flipping_coin}")
        if flipping_coin == player_choice:
            win = min_bet * 2   #current_bet
            depozit += win
            print(f"Выигрыш: {win}")
           # current_bet = min_bet
        else:
            print("Проигрыш")
            min_bet *= 2            # current_bet
            if min_bet > max_bet:     # current_bet
                min_bet = max_bet       # current_bet
        if depozit > max_depozit:
            max_depozit = depozit
        print(f"Текущий депозит: {depozit}")
        if depozit < 0:
          print(f"взяли в долг на последнюю ставку  {-depozit}")
    return steps, max_depozit

step, max_dep = martingale(depozit=100, min_bet=1, max_bet=100)

print("---==============---")
print(f"Колво раундов: {step}")
print(f"Максимальный деп: {max_dep}")