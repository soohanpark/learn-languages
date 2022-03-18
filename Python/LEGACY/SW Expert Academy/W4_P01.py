"""
어렵다... 나중에 다시 한번 도전!!

알고리즘 교수님은 학생들에게 병합 정렬을 이용해 오름차순으로 정렬하는 과제를 내려고 한다.

정렬 된 결과만으로는 실제로 병합 정렬을 적용했는지 알 수 없기 때문에 다음과 같은 제약을 주었다.

N개의 정렬 대상을 가진 리스트 L을 분할할 때 L[0:N//2], L[N//2:N]으로 분할 한다.

병합 과정에서 다음처럼 왼쪽 마지막 원소가 오른쪽 마지막 원소보다 큰 경우의 수를 출력한다.

정렬이 끝난 리스트 L에서 L[N//2] 원소를 출력한다.

알고리즘 교수님의 조건에 따라 병합 정렬을 수행하는 프로그램을 만드시오.

"""
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.leftNode = None
        self.rightNode = None


count = 0


def searchNcompare(nodeA:LinkedList, nodeB:LinkedList):
    if nodeA.value > nodeB.value:
        global count
        count += 1
        if nodeB.rightNode is None:
            nodeB.rightNode = nodeA
        else:
            searchNcompare(nodeA, nodeB.rightNode)

    else:
        if nodeA.rightNode is None:
            nodeA.rightNode = nodeB
        else:
            searchNcompare(nodeB, nodeA.rightNode)


for t in range(int(input())):
    N = int(input())
    data = list(map(LinkedList, input().split())) # 2 2 1 3 5

    tempData = []
    while len(data) != 1:
        if len(data) % 2 == 0:
            for i in range(0, len(data), 2):
                if data[i].value > data[i+1].value: #에러!!
                    count += 1
                    data[i+1].rightNode = data[i]
                    tempData.append(data[i+1])
                else:
                    data[i].rightNode = data[i+1]
                    tempData.append(data[i])

        else:
            for i in range(0, len(data)-2, 2):
                if data[i].value > data[i+1].value:
                    count += 1
                    data[i+1].rightNode = data[i]
                    tempData.append(data[i+1])
                else:
                    data[i].rightNode = data[i+1]
                    tempData.append(data[i])

            tempData.append(data[len(data)-1]) # 마지막


        data = tempData