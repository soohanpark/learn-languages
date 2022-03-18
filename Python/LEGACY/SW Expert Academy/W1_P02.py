"""
5186. [파이썬 S/W 문제해결 구현] 1일차 - 이진수2

0보다 크고 1미만인 십진수 N을 이진수로 바꾸려고 한다. 예를 들어 0.625를 이진 수로 바꾸면 0.101이 된다.

N = 0.625
0.101 (이진수)
= 1*2-1 + 0*2-2 + 1*2-3
= 0.5 + 0 + 0.125
= 0.625

N을 소수점 아래 12자리 이내인 이진수로 표시할 수 있으면 0.을 제외한 나머지 숫자를 출력하고, 13자리 이상이 필요한 경우에는 ‘overflow’를 출력하는 프로그램을 작성하시오.
"""

modDict = {1:0.5,
           2:0.25,
           3:0.125,
           4:0.0625,
           5:0.03125,
           6:0.015625,
           7:0.0078125,
           8:0.00390625,
           9:0.001953125,
           10:0.0009765625,
           11:0.00048828125,
           12:0.000244140625}

res = []

for t in range(int(input())):
    N = float(input())

    i = 1
    temp = ""
    while True:
        if i == 13:
            temp = 'overflow'
            break

        mok = N // modDict[i]
        nameoji = N % modDict[i]

        if (mok == 1) and (nameoji == 0): # 나누어 떨어질 경우
            temp += '1'
            break
        elif mok == 1:
            temp += '1'
            N = nameoji
        else:
            temp += '0'

        i += 1

    res.append(temp)

for i in range(len(res)):
    print("#{} {}".format(i+1, res[i]))