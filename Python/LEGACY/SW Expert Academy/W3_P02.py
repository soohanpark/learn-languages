for t in range(int(input())):
    N = int(input())
    work = []
    for n in range(N):
        work.append(list(map(int, input().split())))

    work.sort(key=lambda work : work[0])

    startTime = work[0][0]
    endTime = work[0][1]
    count = 1
    for i in range(1, N):
        if work[i-1][0] == work[i][0] and endTime > work[i][1]:
            endTime = work[i][1]
        else:
            if endTime <= work[i][0]:
                endTime = work[i][1]
                count += 1


    print("#{} {}".format(t+1, count))