# https://www.acmicpc.net/problem/1043

import sys
import random

if __name__ == "__main__":
    whoKnown = []
    partys = []
    
    N, M = sys.stdin.readline().strip().split(' ')
    N = int(N)
    M = int(M)
    
    Known = int(sys.stdin.readline().strip())
    if Known != 0:
        for i in range(Known):
            whoKnown.append(random.randint(1,N+1))
    else:
        pass
    
    for i in range(M):
        partys.append([ x for x in sys.stdin.readline().strip().split(' ') ])
    
    CanGoParty = M
    
    
    for p in partys:
        FLAG = True
        for i in range(len(p)-1):
            for j in whoKnown:
                if int(p[i+1]) == j:
                    CanGoParty -= 1
                    FLAG = False
                    break
            if FLAG == False:
                break        

    print(CanGoParty)
