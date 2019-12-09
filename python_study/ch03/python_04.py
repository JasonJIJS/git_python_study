# tab 들여쓰기 4칸
# ctrl+shift+F10 : Run단축키
# ctrl + /      : 주석
# __ 는 언더바 2개
# shift + F6 이름변경


def list_append():
    list_data = ['James', 'Robert', 'Lisa', 'Mary']
    list_data.append('test')
    print("{}\n".format(list_data))

def list_insert(data):
    print("--{}--".format("list_insert"))
    print(data)
    print()
    data.insert(1, 'mskim')
    print("{}\n".format(data))


def list_extent(data):
    print("--{}--".format())
# def list_pop():




if __name__ == "__main__":
    list_append()
    list_insert(['James', 'Robert', 'Lisa', 'Mary'])

    # list_insert(['James', 'Robert', 'Lisa', 'Mary'])
    # list_data = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    # print(list_data)
    # print(list_data[0:3])
    # print(list_data[4:8])
    # print(list_data[:3])
    # print(list_data[5:])
    # print(list_data[::2])   # 짝수
    # print(list_data[1::2])  # 홀수
    # del list_data[6]
    # print(list_data)
    # del list_data[6]
    # print()
    # print(6 in list_data)
    # print()
    # print(5 in list_data)
    # myFriends = ['James', 'Robert', 'Lisa', 'Mary']
    # print(myFriends)
    # print()
