def my_student_info_list(std_list):
    for list in range(0, len(std_list)):
        print("**********************")
        print("* 학생이름: {}".format(std_list[list][0]))
        print("* 학급번호: {}".format(std_list[list][1]))
        print("* 전화번호: {}".format(std_list[list][2]))
    print("**********************")
    print("\n")


def my_student_info_tuple(std_tuple):
    for tuple in range(0,2):
        print("**********************")
        print("* 학생이름: {}".format(std_tuple[tuple][0]))
        print("* 학급번호: {}".format(std_tuple[tuple][1]))
        print("* 전화번호: {}".format(std_tuple[tuple][2]))
    print("**********************")
    print("\n")


def my_student_info_dict(std_dict):

    std_dict.keys()
    std_dict.values()
    for num in std_dict.keys():
        print("**********************")
        print("번호 {}".format(num))    #
        print("* 학생이름: {}".format(std_dict[num]["학생 이름"]))
        print("* 학급번호: {}".format(std_dict[num]["학급 번호"]))
        print("* 전화번호: {}".format(std_dict[num]["전화 번호"]))
    print("**********************")
    print("\n")


if __name__ == "__main__":
    std_list = [["현아", "01", "01-235-6789"], ["진수", "02", "01-987-6543"]]
    my_student_info_list(std_list)

    std_tuple = (("현아", "01", "01-235-6789"), ("진수", "02", "01-987-6543"))
    my_student_info_tuple(std_tuple)

    std_dict = {"01": {"학생 이름": "현아", "학급 번호": "01", "전화 번호": "01-235-6789"},
                "02": {"학생 이름": "진수", "학급 번호": "02", "전화 번호": "01-987-6543"}}
    my_student_info_dict(std_dict)