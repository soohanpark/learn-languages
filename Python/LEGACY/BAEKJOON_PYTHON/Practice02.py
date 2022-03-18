# https://www.acmicpc.net/problem/1032

import sys

if __name__ == "__main__":
    N = int(sys.stdin.readline().strip())
    data = []
    for i in range(N):
        data.append(sys.stdin.readline().strip())
    
    data_size = len(data[0])
    for i in data:
        if data_size != len(i):
            print("입력의 길이가 다릅니다!")
    
    result = ""
    temp = None
    for i in range(data_size):
        for j in data:
            if data[0][i] == j[i]:
                temp = data[0][i]
                pass
            else:
                temp = None
                result += "?"
                break
        if temp != None:
            result += temp

    print(result)
    
