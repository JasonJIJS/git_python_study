import random

winner = [1, 2, 3, 9, 12, 23]
bonus = 10
games = []

print("당첨번호: ", winner, " + 보너스번호: ", bonus)
print()

for num in range(0, 5, 1):
    games_n = sorted(random.sample(range(1, 45), 6))    # sorted 오름차순
    games.append(games_n)                               # random.sample(범위, 갯수) : 범위 내 중복 없이 갯수 만큼 반환

for game in games:                          # 로또 5게임중 1게임씩
    win_count = 0
    for winnum in winner:                   # [1, 2, 3, 9, 12, 34] 하나씩 winnum에
        if game.count(winnum) > 0:          # 범위.count(인자) : 범위내에 인자 갯수 카운트
            win_count = win_count + 1
    if win_count == 6:
        print("로또번호: {}\t=> 1등(".format(game))
    elif win_count == 5:
        if game.count(bonus) == 1:
            print("로또번호: {}\t=> 2등".format(game))
        else:
            print("로또번호: {}\t=> 3등".format(game))
    elif win_count == 4:
        print("로또번호: {}\t=> 4등".format(game))
    elif win_count == 3:
        print("로또번호: {}\t=> 5등".format(game))
    else:
        print("로또번호: {}\t=> 꽝!!".format(game))
