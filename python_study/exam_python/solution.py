import random
import numpy as np


def exam_01():
    file_name = "Gettysburg_Address.txt"
    sentence_list = []          # 전체문장 이중리스트
    onesentence_list = []       # 전체문장 한 리스트
    result_dict = {}            # 단어별 딕셔너리
    result_list = []            # 단어별 마지막 결과리스트

    with open(file_name) as f:
        head = f.readline()     # 파일에서 한 줄 읽어오기(첫 줄 무시)
        for oldstr in f:
            newstr = oldstr.replace(",", "")    # 문자열 ',', '.', '-' 제거
            newstr = newstr.replace(".", "")
            newstr = newstr.replace("-", "")
            word = newstr.split()               # 기호들 제거한 한 문장 리스트화
            # print(word)
            sentence_list.append(word)          # 전체 리스트에 한 문장씩 이중리스트 형식으로 추가
            # print(sentence_list)
    # print(sentence_list)                        # 전체 이중 리스트
    for line in sentence_list:
        onesentence_list.extend(line)           # 이중 리스트 => 한 리스트로 한 문장씩 마지막에 추가
        # print(onesentence_list)
    # print(onesentence_list)

    for item in onesentence_list:               # 전체 리스트중 한 단어씩
        # print(item)
        dict = {item: onesentence_list.count(item)}
        # print(onesentence_list.count(item))
        # print("dict : {}".format(dict))
        result_dict.update(dict)                # 딕셔너리에 딕셔너리 데이터 추가
        print("result_dict: {}".format(result_dict))

    result_list = sorted(result_dict.items(), key=lambda x: x[1], reverse=True)
    print("========== 정렬 결과 ==========")
    for line in result_list:
        if line[1] >=3:
            print("{} 단어는 {}번 있습니다.".format(line[0], line[1]))


def exam_02():
    x = int(input("첫번째 수 입력 하시오: "))
    y = int(input("두번째 수 입력 하시오: "))
    z = input("연산자를 선택하시오(+, -, *, /): ")
    print("입력하신 숫자는 {}, {} 이고 연산자는 '{}'입니다".format(x, y, z))
    if z == '+':
        addition = lambda x, y : x + y
        print("사칙연산 결과 : {} 입니다.".format(addition(x,y)))
    elif z == '-':
        subtraction = lambda x, y: x - y
        print("사칙연산 결과 : {} 입니다.".format(subtraction(x, y)))
    elif z == '*':
        multiplication = lambda x, y: x * y
        print("사칙연산 결과 : {} 입니다.".format(multiplication(x, y)))
    elif z == '/':
        division = lambda x, y: x / y
        print("사칙연산 결과 : {} 입니다.".format(round(division(x, y),2)))


def exam_03():
    num = 0
    while(num != 10):
        num = num + 1
        print("나무꾼이 나무를 {}번 찍습니다".format(num))
    print("나무가 넘어갑니다")


def exam_04():
    array = []
    cutarray = []

    array = random.sample(range(1, 10), 6)
    print(array)
    for num in range(2,6):
        cutarray.append(array[num-1])
    cutarray = sorted(cutarray)
    print(cutarray)
    print(cutarray[3])


def solution(array, coms):
    answer = []
    for num in range(0, len(coms)):
        sol1 = arr[coms[num][0]-1 : coms[num][1]]
        sol2 = sorted(sol1)          # 오름차순 정렬
        sol3 = sol2[coms[num][2] - 1]   # 값 출력
        answer.append(sol3)
    print("========== 결과 ==========")
    return answer


if __name__ == "__main__":
    exam_01()
    # exam_02()
    # exam_03()

    # exan_04()
    # array = [1, 5, 2, 6, 3, 7, 4]
    # commands = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]
    # arr = np.array(array)       # 1 * n 배열 생성
    # coms = np.array(commands)   # 3 * 3 배열 생성
    # print(solution(array, coms))