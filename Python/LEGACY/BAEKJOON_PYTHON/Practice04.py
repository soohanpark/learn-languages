# https://www.acmicpc.net/problem/9322
# 제 2 공개키를 제 1 공개키 처럼! 암호문을 평문 처럼! 각 단어의 인덱스를 붙여서 정렬!
import sys

if __name__ == "__main__":
    testCase = int(sys.stdin.readline().strip())

    for repeat_case in range(testCase):
        wordNum = int(sys.stdin.readline().strip())
        firstPublicKey = [f for f in sys.stdin.readline().strip().split(' ')]
        secondPublicKey = [s for s in sys.stdin.readline().strip().split(' ')]
        privateKey = [p for p in sys.stdin.readline().strip().split(' ')]

        pair = dict()

        for first in range(wordNum):
            for second in range(wordNum):
                if firstPublicKey[first] == secondPublicKey[second]:
                    pair[first]=second # 순서 주의!!
                    pass
                else:
                    pass

        result =[]

        for i in range(wordNum):
            result.append(privateKey[pair[i]])

        finalResult = ""
        for i in result:
            finalResult += i + " "

        print(finalResult)