# Section13-1
# 업그레이드 타이핑 게임 제작
# 타이핑 게임 제작 및 기본 완성

import random
import time


words = []       # 영어 단어 리스트 (1000개 로드)
n = 1           # 게임 시도 횟수
cor_cnt = 0     # 정답 갯수

with open('./resource/word.txt', 'r') as f:
    for c in f:
        words.append(c.strip())

print(words)  # 단어 리스트 확인

input("Ready? Press Enter Key!")  # Enter Game Start

start = time.time()  # 시작 시간 기록

while n <= 5:
    random.shuffle(words)
    q = random.choice(words)
    
    print()
    print("*Question # {}".format(n))
    print(q)

    x = input()

    print()

    if str(q).strip() == str(x).strip():
        print("Pass!")
        cor_cnt += 1
    else:
        print("Wrong!")

    n += 1

end = time.time()
et = end - start
et = format(et, ".3f")  # 소수 셋째 자리 출력 (시간)

if cor_cnt >= 3:
    print('합격')
else:
    print('불합격')

# 수행 시간 출력
print("게임 시간: ", et, "초", "정답 개수: {}".format(cor_cnt))
