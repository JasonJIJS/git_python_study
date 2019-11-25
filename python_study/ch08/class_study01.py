class Bicycle():

    def __init__(self, wheel_size=10, color='white'):       # default때 초기값 설정
        self.wheel_size = wheel_size                        # __wheel_size c++과 같은 private 설정시 __ 언더바 2
        self.color = color


    def move(self, speed):
        print("자전거: 시속{} 킬로미터로 전진".format(speed))


    def turn(self, direction):
        print("자전거: {} 회전".format(direction))


    def stop(self):
        print("자전거({}, {}): 정지".format(self.wheel_size, self.color))


    def __str__(self) -> str:                   # 오버라이 / alt + insert 재정의 한 것.
        return str("자전거({}, {})".format(self.wheel_size, self.color))


class Car(Bicycle): # Bicycle 상속 받음
    def stop(self):         # 오버라이딩 한 것
        print("자동차({}, {}): 정지".format(self.wheel_size, self.color))


if __name__ == "__main__":
    my_bicycle = Bicycle()
    # my_bicycle.wheel_size = 26
    # my_bicycle.color = "red"
    # my_bicycle.stop()
    # print(my_bicycle)

    # my_bicycle = Car()
    # my_bicycle.wheel_size = 35
    # my_bicycle.color = 'black'
    # my_bicycle.stop()

    my_bicycle2 = Bicycle(30, "black")
    # my_bicycle2.wheel_size = 30
    # my_bicycle2.color = "black"
    my_bicycle3 = Bicycle()
    [print(c) for c in [my_bicycle, my_bicycle2]]
    print(my_bicycle.wheel_size)

