import random as rnd


def bubble_sort(list):
    for i in range(0, len(list)-1):
        for j in range(0, len(list)-1-i):
            if list[j] > list[j+1]:
                list[j], list[j+1] = list[j+1], list[j]
    return list

# def bubble_sort(random_list):
#     for cnt in range(len(random_list)-1):
#         for i in range(len(random_list)-1):



if __name__ == "__main__":
    random_list = []
    rnd.seed(1)
    for num in range(0, 10):
        random_list.append(rnd.randint(1, 46))
    print("정렬 전 : {}".format(random_list))
    sorted_list = bubble_sort(random_list)
    print("정렬 후 : {}".format(sorted_list))