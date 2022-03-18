"""
5203. [파이썬 S/W 문제해결 구현] 3일차 - 베이비진 게임
0부터 9까지인 숫자 카드 4세트를 섞은 후 6개의 카드를 골랐을 때, 연속인 숫자가 3개 이상이면 run, 같은 숫자가 3개 이상이면 triplet이라고 한다.

게임을 시작하면 플레이어1과 플레이어 2가 교대로 한 장 씩 카드를 가져가며, 6장을 채우기 전이라도 먼저 run이나 triplet이 되는 사람이 승자가 된다.

두 사람이 가져가게 되는 순서대로 12장의 카드에 대한 정보가 주어졌을 때 승자를 알아내는 프로그램을 작성하시오. 만약 무승부인 경우 0을 출력한다.

예를 들어 9 9 5 6 5 6 1 1 4 2 2 1인 경우, 플레이어 1은 9, 5, 5, 1, 4, 2카드를, 플레이어2는 9, 6, 6, 1, 2, 1을 가져가게 된다.

이때는 카드를 모두 가져갈 때 까지 run이나 triplet이 없으므로 무승부가 된다.
"""

# 하.... 둘이 동시에 될때를 모르겠음ㅠㅠㅠ 9/10
for t in range(int(input())):
    deck1 = {}
    deck2 = {}
    for i in range(10):
        deck1[i] = 0
        deck2[i] = 0

    card = list(map(int, input().split()))

    winner = 0

    for i in range(0, 12, 2):
        player1 = card[i]
        player2 = card[i+1]
        deck1[player1] += 1
        deck2[player2] += 1

        if i >= 4:
            if deck1[player1] == 3:
                winner = 1
                break
            elif deck2[player2] == 3:
                winner = 2
                break

            if (player1 ==0):
                if (deck1[player1] > 0 and deck1[player1+1] > 0 and deck1[player1+2] > 0):
                    winner = 1
                    break
            elif (player1 ==9):
                if  (deck1[player1] > 0 and deck1[player1-1] > 0 and deck1[player1-2] > 0):
                    winner = 1
                    break
            else:
                if (deck1[player1-1] > 0 and deck1[player1] > 0 and deck1[player1+1] > 0):
                    winner = 1
                    break
                elif (deck1[player1] > 0 and deck1[player1 + 1] > 0 and deck1[player1 + 2] > 0):
                    winner = 1
                    break
                elif (deck1[player1] > 0 and deck1[player1-1] > 0 and deck1[player1-2] > 0):
                    winner = 1
                    break

            if (player2 == 0):
                if (deck2[player2] > 0 and deck2[player2 + 1] > 0 and deck2[player2 + 2] > 0):
                    winner = 2
                    break
            elif (player2 == 9):
                if (deck2[player2] > 0 and deck2[player2 - 1] > 0 and deck2[player2 - 2] > 0):
                    winner = 2
                    break
            else:
                if (deck2[player2 - 1] > 0 and deck2[player2] > 0 and deck2[player2 + 1] > 0):
                    winner = 2
                    break
                elif (deck2[player2] > 0 and deck2[player2 + 1] > 0 and deck2[player2 + 2] > 0):
                    winner = 2
                    break
                elif (deck2[player2] > 0 and deck2[player2 - 1] > 0 and deck2[player2 - 2] > 0):
                    winner = 2
                    break

    print("#{} {}".format(t+1, winner))