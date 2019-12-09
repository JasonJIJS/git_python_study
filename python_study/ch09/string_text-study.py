def string_split():
    coffee_menu1 = "에스프레소 아메리카노 카페라테 카푸치노"
    print(type(coffee_menu1.split()))
    coffee_list1 = coffee_menu1.split()

    [print(coffee) for coffee in coffee_list1]
    print()

    coffee_menu2 = "에스프레소,아메리카노,카페라테,카푸치노"
    [print(coffee) for coffee in coffee_menu2.split(',')]
    print()

    coffee_menu3 = "에스프레소\n 아메리카노\n 카페라테\n 카푸치노"
    [print(coffee) for coffee in coffee_menu3.split()]
    print()


def string_strip():
    python_str01 = "Python    "
    python_str02 = "aaaaPythonaaaa"
    python_str03 = "aabbPythonbbaa"
    python_str04 = "aaaPythonaaa"
    python_str05 = "##**!!##Python is powerful%%!#"
    python_str06 = "Python is powerful"
    print(python_str01.strip('a'))
    print("중간 문자는 제거 불가능", python_str01.strip('o'))
    print(python_str02.strip('a'))
    print(python_str03.strip('a'))
    print(python_str04.strip('ab'))
    print(python_str05.strip('#*!%'))
    print("중간 공백은 제거 불가능", python_str06.strip())


def string_join():
    name1 = "철수"
    name2 = "영미"
    hello = "님, 주소와 전봐 번호를 입력해 주세요"
    print(name1 + hello)
    address_list = ["서울시", "서초구", "반포대로", "201(반포동)"]
    print(address_list)
    a = " "
    print(a.join(address_list))
    print(",".join(address_list))
    print("^^".join(address_list))


def string_find():
    str_f = "Python code."
    print("찾는 문자열의 위치:", str_f.find("Python"))
    print("찾는 문자열의 위치:", str_f.find("code"))
    print("찾는 문자열의 위치:", str_f.find("n"))
    print("찾는 문자열의 위치:", str_f.find("easy"))

    str_f_se = "Python is powerful. Python is easy to learn"
    print(str_f_se.find("Python", 10, 30))      # 시작 위치, 끝 위치 지정
    print(str_f_se.find("Python", 35))          # 시작 위치 지정

    str_c = "Python is powerful. Python is easy to learn. Python is open."
    print("Python의 개수는?:", str_c.count("Python"))
    print("Powerful의 개수는?:", str_c.count("powerful"))
    print("IPython의 개수는?:", str_c.count("IPython"))

    str_se = "Python is powerful. Python is easy to learn."
    print("Python으로 시작?:", str_se.startswith("Python"))
    print("is로 시작?:", str_se.startswith("is"))
    print(".으로 끝?:", str_se.endswith("."))
    print("learn으로 끝?:", str_se.endswith("learn"))

    str_a = "Python is fast. Python is friendly. Python is open."
    print(str_a.replace('Python', 'Ipython'))
    print(str_a.replace('Python', 'Ipython', 2))

    str_b = '[Python][is][fast]'
    str_b1 = str_b.replace('[','')
    str_b2 = str_b1.replace(']',' ')
    print(str_b)
    print(str_b1)
    print(str_b2)





if __name__ == "__main__":
    # string_split()
    # string_strip()
    # string_join()
    string_find()
