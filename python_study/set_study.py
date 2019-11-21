# 로또번호생성기를 작성하고 당첨번호에 따라 순위를 구하는 프로그램
# 5000원치 로또번호를 생성

import random as rnd
from typing import Set, Any, Union


def lotto_generator():
    lotto_num = set()
    while len(lotto_num) <6:
        lotto_num.add(rnd.randint(1, 46))
    return lotto_num


if __name__ == "__main___":
    rnd.seed(1)         # 동일한 숫자
    num = rnd.randint(1, 46)
    sorted_lotto = list(lotto_generator())



    # print("{} {}". format(lotto_num, len(lotto_num)))
    # set_lotto = lotto_generator()
    # print("로또 번호 : {}".format(set_lotto)) # 정렬된 결과