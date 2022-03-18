# Section07-2
# 파이썬 클래스 상세 이해
# 상속, 다중상속


class Car:
    """
    Parent Class.
    """
    def __init__(self, tp, color):
        self.tp = tp
        self.color = color

    def show(self):
        return "Car Class 'Show Method!'"
    

class BmwCar(Car):  # 상속!
    """
    Child Class. (Bmw)
    """
    def __init__(self, tp, color, car_name):
        self.car_name = car_name
        super().__init__(tp, color)

    def show_model(self) -> None:
        return "Your Car Name : {}".format(self.car_name)


class BenzCar(Car):  # 상속!
    """
    Child Class. (Benz)
    """
    def __init__(self, tp, color, car_name):
        self.car_name = car_name
        super().__init__(tp, color)

    def show_model(self) -> None:
        return "Your Car Name : {}".format(self.car_name)
    
    def show(self):  # Overriden
        return "Car Info: {} {} {}".format(self.car_name, self.tp, self.color)


model1 = BmwCar('sedan', 'red', '520d')
print(model1.color)         # from Parent Class.
print(model1.tp)            # from Parent Class.
print(model1.car_name)      # from Child Class.
print(model1.show())        # from Parent Class.
print(model1.show_model())  # from Child Class.


# Method Overriding(오버라이딩)
model2 = BenzCar('suv', 'black', '220d')
print(model2.show())

# Parent Method Call
model3 = BenzCar('sedan', 'silver', '350d')
print(model3.show())

# Inheritance Info
print(BmwCar.mro())  # 상속 관계도를 보여주는 함수!
print(BenzCar.mro())  # 상속 관계도를 보여주는 함수!


# 예제 2
# 다중 상속
class X:
    pass

class Y:
    pass

class Z:
    pass

class A(X, Y):  # 다중 상속
    pass

class B(Y, Z):  # 다중 상속
    pass

class M(B, A, Z):  # 다중 상속
    pass

print()
print(M.mro())