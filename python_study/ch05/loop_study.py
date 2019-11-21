# for i in [0, 1, 2, 3, 4, 5]:
#     print(i, end= ' ')
# print()
# for i in range(1, 10):
#     print(i, end = " ")
# print()
# for i in range(0, 10, 2): # default:1
#     print(i, end = " ")
# print()
#
# print("{} {}".format(range(0,10), list(range(0,10))))
#
#
# print(list(range(0,20,5)))
# print(list(range(-10,0,2)))
# print(list(range(3,-10,-3)))
# print("아{}".format(list(range(3,-10,-3))))
#
# print(list(range(0,-5,1)))


# gugudan
# gugu(2) 2단 출력 / gugudan() 전체 출력
# gugudan_land() 옆으로

def gugu(dan):
    for x in [dan]:
        for y in range(1, 10):
            print("{} * {} = {}".format(x, y, x * y))
        print()


def gugudan():
    for x in range(2, 10):
        for y in range(1, 10):
            print("{} * {} = {}".format(x, y, x * y))
        print()

def gugudan_land():
    for y in range(1, 10):
        for x in range(2, 10):
            # print("{} * {} = {}".format(x, y, x * y), end= "  ")
            print("{} * {} = {:2}".format(x, y, x * y), end="  ")

        print()



if __name__=="__main__":
    # gugudan()
    # gugu(2)
    # gugudan_land()

    # names = ['James', 'Robert', 'Lisa', 'Mary']
    # scores = [95, 96, 97, 94]
    # for k in range(len(names)):
    #     print("{0} {1}".format(names[k], scores[k]))
    # print()
    # for name, score in zip(names, scores):
    #     print(name, score)


    numbers = [1, 2, 3, 4, 5]
    square1 = []
    square2 = []
    for i in numbers:
        square1.append(i**2)
    for i in numbers:
        if i >=3:
            square2.append(i**2)

    square3 = [i**2 for i in numbers]
    square4 = [i**2 for i in numbers if i>=3]
    square5 = [i**2 for i in numbers if i>= 3]

    print(square1)
    print(square2)
    print(square3)
    print(square4)
    print(square5)





