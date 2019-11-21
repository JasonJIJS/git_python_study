if __name__ == "__main__":
    x =100
    if 90 <= x <= 100:
        print("수")

    if x >= 90:
        if x == 100 :
            print("Perfect")
        else:
            print("Very Good")
    elif (x>=80) and (x<90):
        print("Good")
    else:
        print("Bad")

    for a in [0, 2, 4, 6]:
        print(a)
    print(list(range(0, 10, 1)))

    for a in range(0, 6, 2):
        print(a)