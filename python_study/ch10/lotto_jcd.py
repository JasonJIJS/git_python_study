import random

winner_list = [1, 2, 3, 9, 12, 23]
bonus_list = 10
games = []

print("당첨번호: ", winner_list, " + 보너스번호: ", bonus_list)
print()

for num in range(0, 5, 1):
    games_n = sorted(random.sample(range(1, 46), 6))
    games.append(games_n)

for game in games:
    win_count = 0

    for winnum in winner_list:
        if game.count(winnum) > 0:
            win_count = win_count + 1
    if win_count == 6:
        print("로또번호: {}\t=> 1등(".format(game))
    elif win_count == 5:
        if game.count(bonus_list) == 1:
            print("로또번호: {}\t=> 2등".format(game))
        else:
            print("로또번호: {}\t=> 3등".format(game))
    elif win_count == 4:
        print("로또번호: {}\t=> 4등".format(game))
    elif win_count == 3:
        print("로또번호: {}\t=> 5등".format(game))
    else:
        print("로또번호: {}\t=> 꽝!!".format(game))