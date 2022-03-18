"""
5207. [파이썬 S/W 문제해결 구현] 4일차 - 이진 탐색

서로 다른 정수 N개가 주어지면 정렬한 상태로 리스트 A에 저장한다. 그런 다음 리스트 B에 저장된 M개의 정수에 대해 A에 들어있는 수인지 이진 탐색을 통해 확인하려고 한다.

전체 탐색 구간의 시작과 끝 인덱스를 l과 r이라고 하면, 중심 원소의 인덱스 m=(l+r)//2 이고, 이진 탐색의 왼쪽 구간은 l부터 m-1, 오른쪽 구간은 m+1부터 r이 된다.

이때 M에 속한 어떤 수가 A에 들어있으면서, 동시에 탐색 과정에서 양쪽구간을 번갈아 선택하게 되는 숫자의 개수를 알아보려고 한다.

다음은 10개의 정수가 저장된 리스트 A에서 이진 탐색으로 6을 찾는 예이다.

6은 탐색 과정에서 양쪽을 번갈아 가며 선택하게 된다. 이때 m에 찾는 원소가 있는 경우 방향을 따지지 않는다. M개의 정수 중 조건을 만족하는 정수의 개수를 알아내는 프로그램을 만드시오.
"""

for t in range(int(input())):
    N, M = map(int, input().split())
    A = sorted(list(map(int, input().split())))
    B = list(map(int, input().split()))

    count = 0 # A에 들어 있으면서, 동시에 탐색 구간을 번갈아가며 한 경우!

    for target in B:
        data = A
        leftNright = None
        l = 0 # 한번만 고정되어도 됨.

        while len(data) != 0:
            r = len(data) - 1  # 인덱스
            m = (l+r) // 2 # 기준값 인덱스

            if target < data[m]: #작음 / 왼쪽
                if leftNright == 0:
                    leftNright = False
                    break
                leftNright = 0
                data = data[l:m]

            elif target > data[m]: #큼 / 오른쪽
                if leftNright == 1:
                    leftNright = False
                    break
                leftNright = 1
                data = data[m+1:len(data)] # 마지막 인덱스까지 포함되어야 함

            else:
                leftNright = "COUNT_UP" # 반드시 찾아야지만, Count Up
                break

        if leftNright == "COUNT_UP":
            count += 1

    print("#{} {}".format(t+1, count))