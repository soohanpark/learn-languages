"""
6959. 이상한 나라의 덧셈게임

아래 주석의 코드가 일반적이라 생각했으나, 해당 문제의 특성상 효율적인 알고리즘은 아니다
매 Phase마다 갯수의 문제일뿐 결국 각 case별 text의 사이즈가 동일해지기 때문에
동일한 phase에서 항상 결과가 나오게 된다.
따라서, 여러 케이스를 전부 볼 필요없이 아무거나 하나의 케이스만을 조사하면 결과값이 나온다.
"""

for t in range(int(input())):
    text = input()

    winner = 'B'
    flag = True

    while flag:
        if len(text) == 1:
            print('#{} {}'.format(t+1, winner))
            flag = False
            break
        else:
            newStr = str( int(text[0]) + int(text[1]) )
            text = newStr + text[2:]

        if winner == 'B':
            winner = 'A'
        else:
            winner = 'B'


"""
for t in range(int(input())):
    data = [ input() ]

    winner = 'B'
    flag = True

    while flag:
        tempData = []

        for num in data:
            if len(num) == 1:
                print('#{} {}'.format(t+1, winner))
                flag = False
                break
            else:
                for i in range(len(num)-1): # n-1번 반복
                    temp = num
                    newStr = str( int(temp[i]) + int(temp[i+1]) )
                    newText = temp[:i] + newStr + temp[i+2:]
                    tempData.append(newText)

        data = set(tempData) # 중복되는 케이스 제거
        if winner == 'B':
            winner = 'A'
        else:
            winner = 'B'	
"""