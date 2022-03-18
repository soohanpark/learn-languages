"""
5189. [파이썬 S/W 문제해결 구현] 2일차 - 전자카트

골프장 관리를 위해 전기 카트로 사무실에서 출발해 각 관리구역을 돌고 다시 사무실로 돌아와야 한다.

사무실에서 출발해 각 구역을 한 번씩만 방문하고 사무실로 돌아올 때의 최소 배터리 사용량을 구하시오.

각 구역을 이동할 때의 배터리 사용량은 표로 제공되며, 1번은 사무실을, 2번부터 N번은 관리구역 번호이다.

두 구역 사이도 갈 때와 올 때의 경사나 통행로가 다를 수 있으므로 배터리 소비량은 다를 수 있다.

N이 3인 경우 가능한 경로는 1-2-3-1, 1-3-2-1이며 각각의 배터리 소비량은 다음과 같이 계산할 수 있다.

e[1][2]+e[2][3]+e[3][1] = 18+55+18 = 91

e[1][3]+e[3][2]+e[2][1] = 34+7+48 = 89


e  1  2  3  도착
1  0  18 34
2  48 0  55
3  18 7  0
출발

이 경우 최소 소비량은 89가 된다.
"""

import itertools

for t in range(int(input())):
    N = int(input())
    tee = []
    for n in range(N):
        tee.append(list(map(int, input().split())))

    path = set(itertools.permutations([ x for x in range(1, N) ])) # N-1개의 패스이므로!

    res = 0

    for p in path:
        start = 0
        tot = 0
        for i in p:
            tot += tee[start][i]
            start = i
        tot += tee[start][0]

        if (res == 0) or (res > tot):
            res = tot

    print("#%d %d"%(t+1, res))
