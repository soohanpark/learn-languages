"""
RuntimeError가 나옴.. 시간 복잡도인지, 인덱스 오류인지 모르겠음
"""

for t in range(int(input())):
    # input
    N, D = input().split()
    N = int(N)

    board = []
    for n in range(N):
        board.append(list(map(int, input().split())))

    # calc
    if D == 'up': # 열 병렬
        for i in range(N):
            temp = [board[x][i] for x in range(N)]
            j = 0
            for k in range(N):
                if temp[j] == 0:
                    temp.pop(j)
                    temp.append(0)
                    j -= 1
                elif temp[j + 1] == 0:
                    temp.pop(j + 1)
                    temp.append(0)
                    j -= 1
                elif temp[j] == temp[j + 1]:
                    temp[j] *= 2
                    temp.pop(j + 1)
                    temp.append(0)
                else:
                    pass
                j += 1
            for m in range(N):
                board[m][i] = temp[m]

    elif D == 'down': # 열 병렬
        for i in range(N):
            temp = [board[x][i] for x in range(N)]
            j = N-1
            for k in range(N):
                if temp[j] == 0:
                    temp.pop(j)
                    temp.insert(0,0)
                    j += 1
                elif temp[j - 1] == 0:
                    temp.pop(j - 1)
                    temp.insert(0,0)
                    j += 1
                elif temp[j] == temp[j - 1]:
                    temp[j] *= 2
                    temp.pop(j - 1)
                    temp.insert(0,0)
                else:
                    pass
                j -= 1
            for m in range(N):
                board[m][i] = temp[m]


    elif D == 'left': # 행 병렬
        for i in range(N):
            j = 0
            for k in range(N):
                if board[i][j] == 0:
                    board[i].pop(j)
                    board[i].append(0)
                    j -= 1
                elif board[i][j+1] == 0:
                    board[i].pop(j+1)
                    board[i].append(0)
                    j -= 1
                elif board[i][j] == board[i][j + 1]:
                    board[i][j] *= 2
                    board[i].pop(j + 1)
                    board[i].append(0)
                else:
                    pass
                j += 1

    elif D == 'right': # 행 병렬
        for i in range(N):
            j = N-1 # 끝
            for k in range(N):
                if board[i][j] == 0:
                    board[i].pop(j)
                    board[i].append(0)
                    j += 1
                elif board[i][j-1] == 0:
                    board[i].pop(j-1)
                    board[i].append(0)
                    j += 1
                elif board[i][j] == board[i][j-1]:
                    board[i][j] *= 2
                    board[i].pop(j-1)
                    board[i].append(0)
                else:
                    pass
                j -= 1

    # print
    print('#{}'.format(t+1))
    for line in board:
        for item in line:
            print(item, end=' ')
        print()