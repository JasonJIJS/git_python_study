# file_path = 'two_times_table.txt'

def file_write():
    global file_path
    f = open('two_times_table.txt', 'w')
    for num in range(1,6):
        format_string = "2 X {0} = {1}\n".format(num, 2*num)
        f.write(format_string)
    f.close()


def file_readline():
    global file_path
    f = open("two_times_table.txt")
    line = f.readline()
    while line:
        print(line, end = "")
        line = f.readline()
    f.close()


def file_readlines():
    global file_path
    f = open("two_times_table.txt")
    lines = f.readlines()
    f.close()
    for line in lines:
        print(line, end="")



# def file_freadlines
#     global file_path
#     f = open("two_times_table.txt")
#     for line in f.readlines():
#         print(line, end="" )
#     f.close()


def with_fileio():
    global file_path
    print('===', with_fileio.__name__, '===')
    try:
        with open(file_path,'r')
            file_string = f.read()
            print(file_string)




# 4개의 함수를 정의
if __name__ == "__main__":
    file_write()
    file_readline()
    file_readlines()
    # file_freadlines()












