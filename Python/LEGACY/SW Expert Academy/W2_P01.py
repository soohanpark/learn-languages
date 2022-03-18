"""
5188. [파이썬 S/W 문제해결 구현] 2일차 - 최소합

그림처럼 NxN 칸에 숫자가 적힌 판이 주어지고, 각 칸에서는 오른쪽이나 아래로만 이동할 수 있다.

맨 왼쪽 위에서 오른쪽 아래까지 이동할 때, 지나는 칸에 써진 숫자의 합계가 최소가 되도록 움직였다면 이때의 합계가 얼마인지 출력하는 프로그램을 만드시오.

1 2 3
2 3 4
3 4 5

그림의 경우 1, 2, 3, 4, 5순으로 움직이고 최소합계는 15가 된다. 가능한 모든 경로에 대해 합을 계산한 다음 최소값을 찾아도 된다.
"""

# 다 됐는데 시간 초과....ㅠㅠ

import itertools

for t in range(int(input())):
    N = int(input())
    # 오른쪽(0) n-1개 / 아래(1) n-1개의 조합
    testCase = [0] *(N-1) + [1] * (N-1)
    cases = set(itertools.permutations(testCase))

    board = []
    for i in range(N):
        board.append(list(map(int, input().split())))

    res = 0

    for c in cases:
        i = 0
        j = 0
        result = board[i][j]  # 시작점
        for e in c:
            if e == 1:
                i += 1
            else:
                j += 1

            result += board[i][j]

        if (res == 0) or (res > result):
            res = result

    print('#{} {}'.format(t+1, res))