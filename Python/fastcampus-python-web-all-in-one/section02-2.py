# Section02-2
# 파이썬 기초 코딩
# 몸풀기 코딩 실습

# import this  # Python 철학
import sys

# 파이썬 기본 인코딩 (UTF-8)
print(sys.stdin.encoding)
print(sys.stdout.encoding)

# 출력문
print('hello')

# 변수 선언
myName = 'Soohan Park'

# 조건문
if myName == "Soohan Park":
    print("ok")

# 반복문
for i in range(1, 10):
    for j in range(1, 10):
        print('{} * {} = {}'.format(i, j, i*j))

# 함수 선언
def 인사():
    print('안녕하세요')

인사()

# 클래스
class Cookie:
    pass

# 객체 생성
cookie = Cookie()

print(id(cookie))
print(dir(cookie))