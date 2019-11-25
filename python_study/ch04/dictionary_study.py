def dict_appt(country_name):
    for key in country_name.keys():
        print("key {} type {}".format(key, type(key)))

    for value in country_name.values():
        print("value {} type {}".format(value, type(value)))

    for items in country_name.items():
        print("type {} {}".format(type(items), items) )
        country_name2 = {"한국":"서울", "일본":"도쿄"}
    country_name.update(country_name2)
    print(country_name)
    print("country_name2 {}".format(country_name2))
    print("country_name2" + country_name2)

    country_name2.clear()
    print(country_name2)


def diab():
    pass





if __name__=="__main__":
    country_name = {"영국":"런던", "프랑스":"파리", "스위스":"베른", "호주":"캔버라", "덴마크":"코펜하겐"}
    print(country_name)
    print(type(country_name))
    print(country_name["프랑스"])
    print(len(country_name))
    # list1 = ['a', 'b', 'c']
    # tuple1 = (1, 2, 3, 4)
    # set1 = {'가', '나'}
    # data_dict = {"lst": list1, "tpl": tuple1, "set": set1}
    # for key, value in data_dict.items():
    #     print("key{} -> {}".format(key, value))
    #
    # for key in data_dict.keys():
    #     print("key {} -> {}".format(key, data_dict[key]))
    # print(country_name)
    # country_name["독일"] = "베를린"
    # country_name["호주"] = "멜버른"
    # print(country_name)
    # del country_name['호주']
    # print(country_name)
    # dict_appt(country_name)
    # fruit_code = {"사과":101, "배":102, "딸기":103, "포도":104, "바나나":105}

