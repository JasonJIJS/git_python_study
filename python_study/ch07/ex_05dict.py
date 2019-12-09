# list, tuple, dictionary, set  에서 하나를 선택해 프로그램 작성
#     dictionary, list중
# student_management 패키지 추가
# 학생 정보는 : 학생번호, 학생명, 국어, 영어, 수학, 총점, 평균
# 출력 결과 : 1, 김승영, 90, 90, 90, 270, 90.0
# 1. 메뉴 : 1. 학생목록, 2. 학생추가, 3.학생수정, 4. 학생삭제 5. 종료 메뉴 추가
# 2. 프로그램 수행 시 먼저 student_list.txt 파일을 읽어와 수행
# 3. 각각 메뉴별 수행되도록 작성
# 4. 종료 시 학생목록이 student_list.txt에 저장
# 5. 프린트하여 제출

def menu_print():
    print("*******************************************")
    print("         메뉴를 선택하세요(1~5)")
    print("1.학생목록 2.학생추가 3.학생수정 4.학생삭제 5.종료")
    print("*******************************************")

def stu_list():
    pass


def stu_add():
    pass


def stu_edit():
    pass


def stu_del():
    pass


def menu_exit():
    pass

# 출력 결과 : 1, 김승영, 90, 90, 90, 270, 90.0
# 입력 : 번호, 이름, 국어, 영어, 수학
# std_dict = {"01": {"학생 이름": "지재삼", "국어 성적":90, "영어 성적":90, "수학 성적":90, "총점":270, "평균":90.0},
#             "02": {"학생 이름": "정창도", "국어 성적":90, "영어 성적":90, "수학 성적":90, "총점":270, "평균":90.0}}
#
if __name__ == "__main__":
    # f = open('student_list.txt','w')
    # f.write("")
    # f.close
    # try:
    #     f = open("/home/ji/PycharmProjects/git_python_study/python_study/ch07/student_list.txt", 'w')
    #     print(f)
    #     data = f.read()
    #     print(data)
    # except FileNotFoundError as e:
    #     print("해당 파일이 존재하지 않음", e, sep='\n')
    # finally:
    #     print("finally - done")
    #     f.close()
    # while True:
    # menu_print()
    # stu_list()
    # stu_add()
    # stu_edit()
    # stu_del()
    # menu_exit()
    # in_list=[]
    # print("번호: ",end="")
    # in_list.append(input(""))
    # print("이름: ", end="")
    # in_list.append(input(""))
    # print("국어성적: ", end="")
    # in_list.append(input(""))
    # print("영어성적: ", end="")
    # in_list.append(input(""))
    # print("수학성적: ", end="")
    # in_list.append(input(""))
    # in_list.append(int(in_list[2])+int(in_list[3])+int(in_list[4]))
    # in_list.append(round((int(in_list[2])+int(in_list[3])+int(in_list[4]))/3,-1))
    # print(in_list)
    # std_dict = {in_list[0]: {"학생이름": in_list[1], "국어 성적":in_list[2], "영어 성적":in_list[3], "수학 성적":in_list[4],
    #             "총점":int(in_list[2])+int(in_list[3])+int(in_list[4]),
    #             "평균":(float(in_list[2])+float(in_list[3])+float(in_list[4]))/3 }}
    std_dict = {"학생번호": "01", "학생이름": "지재삼", "국어성적": 90, "영어성적": 90, "수학성적": 90, "총점": 270, "평균": 90.0}
    print(std_dict)
    f = open("/home/ji/PycharmProjects/git_python_study/python_study/ch07/student_list.txt", 'w')
    f.write(std_dict)
    f.close()

    # f = open("/home/ji/PycharmProjects/git_python_study/python_study/ch07/student_list.txt", 'w')
    # f.write(in_list)
    # f.close()

    # print("번호: {}".format(in_list[0]))
    # print("이름: {}".format(in_list[1]))
    # print("국어성적: {}".format(in_list[2]))
    # print("영어성적: {}".format(in_list[3]))
    # print("수학성적: {}".format(in_list[4]))
    # print("합계: {}".format(int(in_list[2])+int(in_list[3])+int(in_list[4])))
    # print("평균: {0:.1f}".format( (float(in_list[2]) + float(in_list[3]) + float(in_list[4]))/3) )
    # print(in_list)
    #std_dict = {"01": {"학생 이름": "지재삼", "국어 성적": 90, "영어 성적": 90, "수학 성적": 90, "총점": 270, "평균": 90.0},
    #             "02": {"학생 이름": "정창도", "국어 성적":90, "영어 성적":90, "수학 성적":90, "총점":270, "평균":90.0}}

    # in_dic[5] = str(int(in_dic[2])+int(in_dic[3])+int(in_dic[4]))
    # in_dic[6] = str(( int(in_dic[2]) + int(in_dic[3]) + int(in_dic[4]) )/3)





