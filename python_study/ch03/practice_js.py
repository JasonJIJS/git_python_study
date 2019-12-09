def prac01():
    numbers = [1, 2, 3, 4, 5]
    square = []
    for i in numbers:
        square.append(i ** 2)
    print(square)


def prac02():
    numbers = [1, 2, 3, 4, 5]
    square = [i**2 for i in numbers]
    print(square)


def prac03():
    # for a in [0, 1, 2, 3, 4, 5]:
        # print(a, a+10)
    [print (a, a+10) for a in [0, 1, 2, 3, 4, 5]]


def prac04():
    myFriends = ['James', 'Robert', 'Lisa', 'Mary']
    for myFriend in myFriends:
        print(myFriends)
    [print (myFriend) for myFriend in myFriends]    # 리스트컴프리헨션


def prac_openfile_write():
    f = open('coffeeShopSalesPracice.txt', 'w')
    for num in range(1, 10):
        format_string = "2 * {0} = {1} \n".format(num, 2*num)
        f.write(format_string)
        print(format_string)
    f.close()


def dict_63():
    country_capital = {"영국":"런던", "1":"런던"}
    print(country_capital)

def prac_with():
    pass

if __name__ == "__main__":
    dict_63()