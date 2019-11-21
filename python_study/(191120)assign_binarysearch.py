import random as rnd


def bubble_sort(list):
    for i in range(0, len(list)-1):
        for j in range(0, len(list)-1-i):
            if list[j] > list[j+1]:
                list[j], list[j+1] = list[j+1], list[j]
    return list


def binary_search(searchkey):
    left = len(sorted_list)-len(sorted_list)
    right = len(sorted_list)-1
    mid = left + right // 2
    print(  "mid 위치: {}".format(mid+1))
    print( "left 위치: {}".format(left+1))
    print("Right 위치: {}".format(right+1))

    while True:
        if searchkey > sorted_list[mid]:
            left = mid + 1
            if sorted_list[left] == sorted_list[right]:
                break
        print("찾는 값의 위치는 {}번째 입니다.".format(left))
        elif searchkey < sorted_list[mid]:
            right = mid + 1
            if sorted_list[left] == sorted_list[right]:
                break
        print("찾는 값의 위치는 {}번째 입니다.".format(left))



# if num > sorted_list[mid]:

    # print("left :{}".format(left))
    # print("Right :{}".format(right))
    # print("mid :{}".format(mid))

if __name__ == "__main__":
    random_list = []
    rnd.seed(1)
    for num in range(0, 10):
        random_list.append(rnd.randint(1, 46))
    # print("정렬 전 : {}".format(random_list))
    sorted_list = bubble_sort(random_list)
    print("정렬 후 : {}".format(sorted_list))
    binary_search(42)
