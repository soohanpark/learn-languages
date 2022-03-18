"""
7675. 통역사 성경이

성경이는 대통령 직속 통역관이다.

대통령은 사람 이름을 외우는 것을 굉장히 중요시 한다.

따라서 외국 대사와의 대화에서 나오는 모든 이름을 외워달라고 성경이에게 부탁했다.

외국 대사는 총 N개의 문장을 말했다.

각 문장의 마지막 단어는 세 가지 구두점 ‘.’, ‘?’, ‘!’ 중 하나를 마지막에 포함한다.

문장은 대소문자 알파벳와 숫자로 이루어진 단어들이 공백을 사이에 두고 구성되어 있으며, 예외적으로 마지막 단어는 구두점으로 끝나게 된다.

이름은 대문자 알파벳으로 시작하며 나머지는 소문자 알파벳인 단어들이다.

예외적으로, 단어의 마지막이 구두점일 경우에도 이름이며, 대문자 한글자도 이름이다.

성경이는 대통령을 위해서 외국 대사와의 대화를 문서로 받아서 이름이 몇 번 나오는 지를 알려줘야 한다.

N개의 문장을 받아서 문장 별로 이름의 개수를 구하여라.
"""


for t in range(int(input())):
    N = int(input())
    inputWord = input()
    sentences = []
    lastPoint = 0
    for i in range(len(inputWord)):
        if inputWord[i] in ('.', '?', '!'):
            sentences.append(inputWord[lastPoint:i].strip())
            lastPoint = i+1
    #print(sentences)
    # sentences 를 space로 나누어 각 단어별 판별
    # 첫글자 대문자 이면서 나머지 소문자
    # 마지막 글자 구두점 (구두점 전부 제거! 어치피 LoL! 같이 마지막 구두점이여도 위 조건 안맞으면 끝)
    # 대문자 한글자

    res = []
    for s in sentences:
        count = 0
        words = s.split()
        for w in words:
            if len(w) == 1 and w[0].isupper() and w.isalpha():
                count += 1
            elif w[0].isupper() and w[1:].islower() and w.isalpha():
                count += 1
        res.append(count)

    print('#{}'.format(t+1), end=' ')
    for r in res:
        print("{}".format(r), end=' ')
    print('')