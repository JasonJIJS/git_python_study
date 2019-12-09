# 1, 2, 3, 9, 12, 13, 보너스 10
# 1등 6개 / 2등 5개 + 보너스 / 3등 5개 / 4등 4개 / 5등 3개
import random

lotto_winning = [1, 2, 3, 9, 12, 13]    # 당첨 번호
bonus_num = [10]                        # 보너스 번호

lotto = []                              # 로또 1게임
games = []                              # 로또 5게임

def produce_lotto():
    print("당첨 번호 :",lotto_winning," + 보너스 번호 :",bonus_num)
    for game in range(0, 5, 1):
        lotto = sorted(random.sample(range(1, 46), 6))
        games.append(lotto)


def confirm_lotto():
    for lotto in games:                     # 전체 5게임(games)중 1게임(lotto)
        print("====이번주 로또 번호 : {}, 보너스 번호 : {}====".format(lotto_winning, bonus_num))
        print("====   내 로또 번호 : {}   ====".format(lotto))
        samenum_list = []                   # 당첨 번호랑 내 로또 동일번호 리스트
        samenum_cnt = 0
        bonus = 0
        for num2 in lotto_winning:      # 당첨번호(lotto_winning)의 한 요소를 num2으로
            # print(num2) 확인0
            if lotto.count(num2) > 0:   # 1게임(lotto)범위와 당첨번호(lotto_winning)의 한 요소가 같다면
                # print("한게임 로또번호{}".format(lotto)) 확인0
                samenum_list.append(num2)   # samenum_list에 같은 번호를 추가
                # print("num2 {}".format(sorted(samenum_list)))
                samenum_cnt = samenum_cnt + 1
                # print("same_num:{}, samenum_cnt: {}".format(samenum_list, samenum_cnt))
            # print("ddd: {}llllllllllllllll{}".format(num2,lotto_winning))

        for bonusnum in bonus_num:
            for num2 in lotto:
                if bonusnum == num2:
                    bonus = bonus + 1

        print("* 보너스 번호(불일치0, 일치1) : {} *".format(bonus))
        print("* 일치하는 숫자: {}, 일치하는 숫자 갯수 : {}개 입니다. *".format(samenum_list, samenum_cnt))

        if samenum_cnt <=2:
            print("* 꽝 다음 기회를 이용해주세요 *\n")
        elif samenum_cnt == 3:
            print("* 5등입니다. 일치하는 숫자 갯수 : {}개 입니다. *\n".format(samenum_cnt))
        elif samenum_cnt == 4:
            print("* 4등입니다. 일치하는 숫자 갯수 : {}개 입니다. *\n".format(samenum_cnt))
        elif samenum_cnt == 5:
            if bonus == 1:
                print("* 2등입니다. 일치하는 숫자 갯수 : {}개 + 보너스 번호 : {}개 입니다. *\n".format(samenum_cnt, bonus_num))
            else:
                print("* 3등입니다. 일치하는 숫자 갯수 : {}개 입니다. *\n".format(samenum_cnt))
        else:
            print("* 1등입니다. 일치하는 숫자 갯수 : {}개 입니다. *\n".format(samenum_cnt))

if __name__ == "__main__":

    produce_lotto()
    confirm_lotto()




