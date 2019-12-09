


def anony(x):
    return x ** 2  # res = res = (lambda x: x**2) 같은 의미


if __name__ == "__main__":
    res = (lambda x: x**2)(3)

    mySquare = lambda x : x ** 2
    print(mySquare(9))
    print(res)

    sumList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(sum(sumList))
    print(len({1:'Thomas', 2:'Edward', 3:'Henry'}))

    scores = [90, 80, 95, 85]
    score_sum = 0
    subject_num = 0
    for score in scores:
        score_sum = score_sum + score
        subject_num = subject_num + 1
    average = score_sum / subject_num

    list1 = [1, 2, 3, 4, 5]
    # for i in list1:
    #     print(i**2)

    [print(i ** 2, end = ' ') for i in list1 ]
    print()
    [print(i **2, end=' ') for i in list1 if i % 2 == 1 ]


