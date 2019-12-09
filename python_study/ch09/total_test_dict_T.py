file_name = "coffeeShopSales.txt"

if __name__ == "__main__":
    f = open(file_name)
    header = f.readline()
    headerList = header.split()
    dict_sale = []
    list_sale = []
    saledate = []
    espresso = []
    americano = []
    cafelatte = []
    cappucino = []

    for line in f:
        dataList = line.split()
        saledate.append(dataList[0])
        espresso.append(int(dataList[1]))
        americano.append(int(dataList[2]))
        cafelatte.append(int(dataList[3]))
        cappucino.append(int(dataList[4]))
    f.close()

    for i in range(0,4):
        list_sale = {headerList[0]:saledate[i], headerList[1]:espresso[i], headerList[2]:americano[i],
                     headerList[3]:cafelatte[i], headerList[4]:cappucino[i]}
        dict_sale.append(list_sale)

    [print(data) for data in dict_sale]

    result = {}
    stat = {}
    for coffee in dict_sale:
        for k in coffee.keys():
            if k != '날짜':
                result[k] = result.get(k, 0) + int(coffee[k]) # 없을때의 리턴값을 정해 줌
                stat[k] = stat.get(k, 0) + 1

    print(result)
    print(stat)
    print()
    for p, c in zip(result.keys(), stat.keys()):
        print("{:} 판매량{:}, 하루 평균{:.2f}".format(p, result[p], result[p]/stat[c]))
