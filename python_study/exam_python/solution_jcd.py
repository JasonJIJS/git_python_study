import random
import numpy as np


def num1prob():
    file_name = "Gettysburg_Address.txt"

    data = []
    data_list = []
    final_dict = {}
    final_result = []

    with open(file_name) as f:
        head = f.readline()
        print(head)
        for line in f:
            line_split = line.split(" ")
            data.append(line_split)
    for line in data:
        data_list.extend(line)
    for num in range(0, len(data_list)):
        data_list[num] = data_list[num].strip("\n")
        data_list[num] = data_list[num].strip(".")
        data_list[num] = data_list[num].strip(",")
        data_list[num] = data_list[num].strip("-")
    for item in data_list:
        dict = {item: data_list.count(item)}
        final_dict.update(dict)
    del final_dict[""]
    final_result = sorted(final_dict.items(), key=lambda x: x[1], reverse=True)

    print("=== 정렬 결과 ===")
    for line in final_result:
        print("{} 단어는 {}번 나타났습니다.".format(line[0], line[1]))


def num2prob():
    data1 = input("첫번째 숫자를 입력하시오 : ")
    data2 = input("두번째 숫자를 입력하시오 : ")
    operator = input("연산자를 입력하시오 (+, -, x, /):")

    if operator == "+":
        cal = lambda x, y : int(x) + int(y)
    elif operator == "-":
        cal = lambda x, y: int(x) - int(y)
    elif operator == "x":
        cal = lambda x, y: int(x) * int(y)
    elif operator == "/":
        if int(data2) == 0:
            print("나누는 수가 0이므로 불가능합니다.")
            return
        cal = lambda x, y: int(x) / int(y)
    print(cal(data1, data2))


def num3prob():
    count = 1
    while True:
        print("나무꾼이 나무를 {}번 찍습니다".format(count))
        count = count + 1
        if count == 11:
            print("나무가 넘어갑니다")
            break


def solution(arr, comms):
    answer = []
    for num in range(0, len(comms)):
        tmp1 = arr[comms[num][0]-1:comms[num][1]]
        tmp2 = sorted(tmp1)
        tmp3 = tmp2[comms[num][2]-1]
        answer.append(tmp3)
    return answer


if __name__ == "__main__":
    num1prob()
    # num2prob()
    # num3prob()

    # array = [1, 5, 2, 6, 3, 7, 4]
    # commands = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]
    #
    # arr = np.array(array)
    # coms = np.array(commands)
    # print(solution(arr, coms))