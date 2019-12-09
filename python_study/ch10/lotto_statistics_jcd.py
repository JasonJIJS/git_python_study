if __name__ == "__main__":
    file_name = "lotto_번호통계.csv"

    data_list = []
    num_list = []

    for num in range(1, 46):
        num_dict = {"{}".format(num): 0}
        num_list.append(num_dict)

    with open(file_name) as f:
        for line in f:
            line_split = line.split(",")
            line_split[6] = line_split[6].strip()
            data_list.append(line_split)
        print(data_list)

        for data in data_list:
            for num in range(0, len(num_list)):
                num_list[num]["{}".format(num+1)] = num_list[num]["{}".format(num+1)] + data.count("{}".format(num+1))

    print(num_list)

    for num in range(0, len(num_list)):
        for key, value in num_list[num].items():
            print("{:2}번 번호는 총 {}회 출현".format(key, value))


