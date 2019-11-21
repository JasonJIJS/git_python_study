# tab 들여쓰기 4칸
# ctrl+shift+F10 : Run단축키
# ctrl + /      : 주석
# __ 는 언더바 2개

if __name__ == "__main__":
    print(1 + 1)
    print(type(1 + 1))
    print(17)
    print(0o11)
    print(bin(17))
    print(oct(17))
    print(hex(17))
    print(type(True))
    print(5 == 3)
    print(5 != 3)
    print(5 < 3)
    print(5 > 3)
    print("Hello Python")
    str1 = "hello python"
    print(str1)
    print("{} first python ex{}".format(str1, 1))
    print(str1 * 3)
    print()
    student1 = [90, 91, 92]
    print(type(student1))
    print(student1)
    print(student1[0])
    print(len(student1))
    print(student1[-1])
    print()
    student1[1] = 80
    print(student1)
    print()
    student2 = ['김승영', 90, 90, 90]
    print(student2)
    print()
    student3 = ['김성훈', 90, 70, 80]
    print(student2 + student3)
    print(type(student2 + student3))
    print(student3 * 2)
    print()
    for t in student3:          # for 반복문
        print(t)
    print()
    for t in student3[0:len(student3):2]:          # for 반복문
        print(t)
    print()

