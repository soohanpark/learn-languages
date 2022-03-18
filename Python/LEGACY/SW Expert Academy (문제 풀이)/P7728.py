"""
7728. 다양성 측정
다 했는데 파이썬은 없음 ㅠㅠㅠ
"""

for t in range(int(input())):
    X = input()

    numDict = {0:0, 1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0}

    for x in X:
        numDict[int(x)] += 1

    count = 0
    for i in range(len(numDict)):
        if numDict[i] != 0:
            count += 1

    print("#{} {}".format(t+1, count))