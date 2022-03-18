
#####################################################################################################################
# BFS와 DFS(반복, 재귀) 구현
#####################################################################################################################

class Graph:
    """
    생성자 기본 값 : 0 (아무런 노드들이 생성되지 않음)
    """

    class Node: # 노드 구현
        data = None # 값
        adj = None # 인접한 노드들 저장할 변수 (list)
        mark = None # 방문 여부
        def __init__(self, _data:int):
            self.data = _data
            self.mark = False
            self.adj = list()

    nodes = [] # 노드들을 저장할 배열

    def __init__(self, size:int = 0): # 노드 생성 (그래프 초기화)
        for i in range(size):
            self.nodes.append(self.Node(i))


    def addEdge(self, i1, i2): # 노드 간 연결 관계 형성
        n1 = self.nodes[i1]
        n2 = self.nodes[i2]

        if n2 not in n1.adj:
            n1.adj.append(n2)
        if n1 not in n2.adj:
            n2.adj.append(n1)


    def visit(self, _node:Node): # 노드 방문
        print(_node.data, end=" ")


    def dfs(self, n:int = 0):
        root = self.nodes[n] # 해당 인덱스로 노드 리스트에서 노드를 가져와 현재 노드로 지정
        stack = [ root ] # stack을 만들고, 현재 노드를 stack에 집어 넣음
        root.mark = True # stack에 들어갔다고 표시

        while len(stack) != 0: # 탐색 시작
            temp = stack.pop() # stack에서 노드를 꺼내옴 (1) | 맨 뒤에서 꺼내옴

            for a in temp.adj: # 해당 노드의 child 노드들을 stack에 넣음 (2)
                if a.mark is False:
                    a.mark = True # stack에 들어갔다고 표시
                    stack.append(a)

            self.visit(temp) # 현재 노드의 값 출력 (3)


    def bfs(self, n:int = 0):
        root = self.nodes[n] # 해당 인덱스로 노드 리스트에서 노드를 가져와 현재 노드로 지정
        queue = [ root ] # queue를 만들고, 현재 노드를 queue에 집어 넣음
        root.mark = True # queue에 들어갔다고 표시

        while len(queue) != 0:
            temp = queue.pop(0) # 맨 앞에서 꺼내옴

            for a in temp.adj:
                if a.mark is False:
                    a.mark = True
                    queue.append(a)

            self.visit(temp)


    def dfsR(self, _node:Node): # 재귀 형태의 DFS는 노드를 받는 형태가 되어야 한다
        if _node is None: return

        _node.mark = True

        self.visit(_node) # 재귀는 출력을 먼저 해준다! (중요)

        for a in _node.adj:# 호출이 되지 않은 child 노드들을 호출해준다
            if a.mark is False:
                self.dfsR(a)

    def dfsRi(self, n:int = 0):
        temp = self.nodes[n]
        self.dfsR(temp)


    def test_clear_all_flag(self): # test를 위해 flag 초기화 하는 함수
        for n in self.nodes:
            n.mark = False

#####################################################################################################################
"""
  0
 /
1 -- 3    7
|  / | \ /
| /  |  5
2 -- 4   \ 
          6 - 8
"""

if __name__ == '__main__':
    g = Graph(9)

    g.addEdge(0, 1)
    g.addEdge(1, 2)
    g.addEdge(1, 3)
    g.addEdge(2, 3)
    g.addEdge(2, 4)
    g.addEdge(3, 4)
    g.addEdge(3, 5)
    g.addEdge(5, 6)
    g.addEdge(5, 7)
    g.addEdge(6, 8)

    print("** DFS **")
    g.dfs()
    g.test_clear_all_flag()
    print("\n")

    print("** BFS **")
    g.bfs(3)
    g.test_clear_all_flag()
    print("\n")

    print("** DFS (Recursion) **")
    g.dfsRi(0)
    g.test_clear_all_flag()
    print("\n")