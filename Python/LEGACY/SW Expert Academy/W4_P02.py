"""
퀵 정렬을 구현해 N개의 정수를 정렬해 리스트 A에 넣고, A[N//2]에 저장된 값을 출력하는 프로그램을 만드시오.
"""


for t in range(int(input())):
    N = int(input())
    data = sorted(map(int, input().split()))
    print("#{} {}".format(t+1, data[N//2]))