# student_management 패키지 추가
# 학생 정보는 : 학생번호, 학생명, 국어, 영어, 수학, 총점, 평균
# 출력 결과 : 1, 김승영, 90, 90, 90, 270, 90.0
# 1. 메뉴 : 1. 학생목록, 2. 학생추가, 3.학생수정, 4. 학생삭제 5. 종료 메뉴 추가
# 2. 프로그램 수행 시 먼저 student_list.txt 파일을 읽어와 수행
# 3. 각각 메뉴별 수행되도록 작성
# 4. 종료 시 학생목록이 student_list.txt에 저장
# 5. 프린트하여 제출
# 출력 결과 : 1, 김승영, 90, 90, 90, 270, 90.0
# 입력 : 번호, 이름, 국어, 영어, 수학
# std_dict = {"01": {"학생 이름": "지재삼", "국어 성적":90, "영어 성적":90, "수학 성적":90, "총점":270, "평균":90.0},
#             "02": {"학생 이름": "정창도", "국어 성적":90, "영어 성적":90, "수학 성적":90, "총점":270, "평균":90.0}}
def load_list():
    f = open("/home/ji/PycharmProjects/git_python_study/python_study/ch07/student_list.txt", 'r')
    line = f.readline()
    while line:
        stdinfo=line.split(',')     # 구분자를 이용해서 list로 읽는다.
        total = 0
        total = int(stdinfo[2]) + int(stdinfo[3]) + int(stdinfo[4])
        student=[int(stdinfo[0]),stdinfo[1],int(stdinfo[2]),int(stdinfo[3]),int(stdinfo[4]),total,round(total/float(3),1)]
        total_list.append(student)
        line = f.readline()         # line이 false가 되면 while탈출
    f.close()


def menu_print():
    print("*******************************************")
    print("         메뉴를 선택하세요(1~5)")
    print("1.학생목록 2.학생추가 3.학생수정 4.학생삭제 5.종료")
    print("*******************************************")


def stu_list():
    print("*******************************************")
    print("번호 이름  국어 영어 수학 총점  평균")
    for i in total_list:
        format_string = "{0:2} {1:3}  {2}  {3}  {4}  {5:2}  {6:4}\n".format(i[0],i[1],i[2],i[3],i[4],i[5],i[6])
        print(format_string)


def stu_add():
    in_list = []
    print("번호: ", end="")
    in_list.append(input(""))
    print("이름: ", end="")
    in_list.append(input(""))
    print("국어성적: ", end="")
    in_list.append(input(""))
    print("영어성적: ", end="")
    in_list.append(input(""))
    print("수학성적: ", end="")
    in_list.append(input(""))
    total = 0
    total = int(in_list[2]) + int(in_list[3]) + int(in_list[4])
    in_list.append(total)
    in_list.append(round(total/ float(3),1))
    total_list.append(in_list)


def stu_edit():
    num = int(input("변경할학생 순서입: "))
    total_list[num][0] = input("학생번호: ")
    total_list[num][1] = input("학생이름: ")
    total_list[num][2] = input("국어성적: ")
    total_list[num][3] = input("영어성적: ")
    total_list[num][4] = input("수학성적: ")
    total_list[num][5] = int(total_list[num][2]) + int(total_list[num][3]) + int(total_list[num][4])
    total_list[num][6] = round((float(total_list[num][2]) + float(total_list[num][3]) + float(total_list[num][4]))
                               / 3, 1)


def stu_del():
    num = int(input("변경할학생 순서입력: ")-1)
    total_list.remove(total_list[num])
    print(total_list)


def menu_exit():
    print("이용해주셔서 감사합니다.")
    f = open("/home/ji/PycharmProjects/git_python_study/python_study/ch07/student_list.txt", 'w')
    for i in total_list:
        format_string = "{},{},{},{},{}\n".format(i[0],i[1],i[2],i[3],i[4])
        f.write(format_string)
    f.close()


if __name__ == "__main__":
    total_list = []
    load_list()     # 텍스트 파일 읽어오기
    while True:
        menu_print()
        num = (input("*메뉴를 선택하세요*: "))
        if num == '1':
            stu_list()
        elif num == '2':
            print("*추가할 학생의 정보를 입력하세요* ")
            stu_add()
        elif num == '3':
            print("*몇번 째 학생을 수정 할까요?* ")
            stu_edit()
        elif num == '4':
            print("*몇번 째 학생을 삭제 할까요?* ")
            stu_del()
        elif num == '5':
            menu_exit()
            break
        else:
            print("번호를 다시 입력하세요")

