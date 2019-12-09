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

    print(dict_sale[0]['날짜'], dict_sale[0])

    # print(dict_sale0.keys(), dict_sale0.values(), dict_sale0.items())




# total_sum = [sum(espresso), sum(americano), sum(cafelatte), sum(cappucino)]
# total_mean = [sum(espresso)/len(espresso), sum(americano)/len(americano),
#               sum(cafelatte)/len(cafelatte),sum(cappucino)/len(cappucino) ]

# for k in range(len(total_sum)):
#     print('[{0}] 판매량'.format(headerList[k+1]))
#     print('-나흘 전체: {0}, 하루 평균: {1}'.format(total_sum[k], total_mean[k]))



