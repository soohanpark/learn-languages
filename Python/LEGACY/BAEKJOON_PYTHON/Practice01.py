# https://www.acmicpc.net/problem/1026

import sys

if __name__ == "__main__":
    N = int(sys.stdin.readline().strip())
    A = [ int(x) for x in sys.stdin.readline().strip() if x != ' ' ]
    B = [ int(x) for x in sys.stdin.readline().strip() if x != ' ' ]
    
    if len(A) + len(B) != 2*N:
        print("조건을 잘못 입력하셨습니다!")

    A.sort()
    B.sort(reverse = True)

    result = 0
    for i in range(N):
        result += (A[i]*B[i])

    print(result)
