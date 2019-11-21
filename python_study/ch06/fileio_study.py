try:
    f = open("/home/ji/PycharmProjects/git_python_study/python_study/ch06/print_study.py", 'r')
    print(f)
    data = f.read()
    print(data)
except FileNotFoundError as e:
    print("해당 파일이 존재하지 않음",  e, sep='\n')
finally:
    print("finally - done")
    f.close()


try:
    f= open("/home/ji/PycharmProjects/git_python_study/python_study/ch06/test.txt", 'x')
    f.write(data)
except FileExistsError as e:
    f = open("/home/ji/PycharmProjects/git_python_study/python_study/ch06/test.txt", 'w')
    f.write(data)
    print("해당 파일이 존재", e, sep='\n')
finally:
    print("finally - done")
    f.close()

print("done")

