import random

if __name__ == "__main__":
    print(random.random())

    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)
    print('주사위 두 개의 숫자: {0}, {1}'.format(dice1, dice2))

    print(random.randrange(0,11,2))

    num1 = random.randrange(1, 10, 2)
    num2 = random.randrange(0, 100, 10)
    print('num1: {0}, num2: {1}'.format(num1, num2))

    menu = ['비빔밥', '된장찌깨', '볶음밥', '불고기', '스파게티', '피자', '탕수육']
    print(random.choice(menu))

    # print(random.sample([1, 2, 3, 4, 5], 2))

    print(random.sample([1, 2, 3, 4, 5, 6, 7], 6))



