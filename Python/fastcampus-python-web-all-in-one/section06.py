# Section 06
# 파이썬 함수식 및 람다 (lambda)

# 함수 정의 방법
# def 함수명(param.):
#    code

# 함수 선언 위치 중요

# 가변 인자 (*args, **kwargs)  # args, kwargs는 변수명이다!
# *args: 튜플 형태로 받음!
# *kwargs: 딕셔너리 형태로 받음!

# enumrate(튜플같은 순서가 없는 것) => 인덱스를 만들어서 반환!

# 중첩 함수 (클로저)
# - 함수 안에 함수가 있는 것.
# - 메모리 관리를 효율적으로 할 수 있음.
# - 파이썬 데코레이터 클로저 `검색해볼 것!!`
def nested_func(num):
    def func_in_func(num):
        print('>>>', num)
    print('in_func')
    func_in_func(num + 10000)

nested_func(10000)

# 함수 인자 및 반환값 타입 명시
def func_mul3(x : int) -> list:
    resultList = []
    # code
    return resultList


# 람다식
# - 메모리 절약
# - 가독성 향상
# - 코드 간결
# 함수는 객체 생성 -> 리소스(메모리) 할당
# 람다는 즉시 실행(Heap 초기화) -> 메모리 초기화

# 일반적 함수 -> 변수 할당
def mul_10(num:int) -> int :
    return num * 10

var_func = mul_10
print(var_func)
print(type(var_func))

# 람다식
lambda_mul_10 = lambda x: x*10

print(lambda_mul_10(10))
