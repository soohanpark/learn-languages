# Section07-1
# 파이썬 클래스 상세 이해
# Self, 클래스, 인스턴스 변수

# 클래스 변수: 직접 사용 가능, 객체 보다 먼저 생성
# 인스턴스 변수: 객체마다 별도로 존재

# 예제1
class UserInfo:
    # 속성
    name = None
    # 메서드
    def __init__(self, name=None):
        self.name = name
        print('초기화')

    def user_info_p(self):
        print("Name:", self.name)

user = UserInfo("Park")
user.user_info_p()

user2 = UserInfo()

print(user)
print(id(user))
print(user2.__dict__)
print(id(user2))
print(UserInfo)


# 예제 2
# self의 이해
class SelfTest:
    # 클래스 메서드! (인스턴스가 아닌, 클래스에서 호출해주어야 함)
    def function1():
        print('funtion1 called!')
    
    # 인스턴스 메서드! (self를 통해 해당 인스턴스를 지정. 인스턴스를 통해 호출을 해주어야 함)
    def function2(self):
        print('function2 called!')

self_test = SelfTest()

SelfTest.function1()
self_test.function2()
SelfTest.function2(self_test)  # 인스턴스를 매개변수로 지정해주어서 사용!


# 예제 3
# 클래스 변수, 인스턴스 변수
class WareHouse:
    # 클래스 변수
    stock_num = 0

    # 인스턴스 변수는 이렇게 __init__ 안에서 생성해주는 것으로 하자!
    def __init__(self, name):
        # 인스턴스 변수
        self.name = name
        self.age = 15
        WareHouse.stock_num += 1
    
    def __del__(self):  # 인스턴스 소멸 시 호출되는 매직 매서드
        WareHouse.stock_num -= 1
   
worker1 = WareHouse("123123")
worker2 = WareHouse("456456")
worker3 = WareHouse("789789")

print(worker1.__dict__)
print(worker2.__dict__)
print(worker3.__dict__)
print(WareHouse.__dict__)

print(worker1.stock_num)
print(worker2.stock_num)

del worker1

print(worker3.stock_num)
