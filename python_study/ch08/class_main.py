from python_study.ch08.class_def import Car         # package.파일명 : 모듈

if __name__ == "__main__":
    myCar = Car()           # alt + enter
    myCar2 = Car(size = 20, color = "red")
    myCar3 = Car(size = 20)

    car_list = [myCar, myCar2, myCar3]


    print("자동차 총 샌산 대수 : {}".format(Car.instance_count))
    [print(car) for car in car_list]

    Car.instance_count = Car.instance_count + 1
    myCar4 = Car()

    myCar.set_speed(100)
    myCar.auto_cruse()

    myCar2.set_speed(200)
    myCar2.auto_cruse()

    Car.check_type(20)
    Car.check_type(15)

    Car.count_instance()



