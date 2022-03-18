"""
ALOHA 구현 

- Pure ALOHA
- Slotted ALOHA

<유의사항>
- 패킷이 발생하는 빈도 수는 exponential random
"""

#packages
import math
import random
from matplotlib import pyplot as plt


sample = 10000


# Accumulation startPoint!
def packetGenerator(sample:int, lamda, tau):
    """
    exponential random = -1*(1/lamda)*ln(Unit)
    """

    packetStart = []
    packetEnd = []
    packetPoint = 0

    for i in range(sample):
        packetPoint += -1 * (1 / lamda) * math.log(random.random()) # Accumulation
        packetStart.append(packetPoint)
        packetEnd.append(packetPoint + tau) # last value of packetEnd is T

    return packetStart, packetEnd


def collisionCheckPureALOHA(sample:int, packetStart:list, packetEnd:list): # Count of success pkts
    count = 0
    for i in range(sample):
        # Three Cases : 1. First pkt, pkts, and Last pkt
        if i == 0: # First pkt
            if packetEnd[0] <= packetStart[1]:
                count += 1

        elif i == sample-1: # Last pkt
            if packetEnd[i-1] <= packetStart[i]:
                count += 1

        else: # pkts
            if (packetEnd[i-1] <= packetStart[i]) and (packetEnd[i] <= packetStart[i+1]):
                count += 1

    return count


def collisionCheckSlottedALOHA(sample:int, packetStart:list, packetEnd:list, tau, T):
    # slot duration tau
    count = 0

    startRange = packetStart[0] - (2 * tau) # 앞의 빈 슬롯들 최대한 건너뛰기 위해 / 2*tau 안전하게 넉넉히 여유분을 둠
    endRange = startRange + tau

    i = 0
    littleCount = 0
    while (endRange <= T) and not(i == sample): #endRange가 T 보다 커지면 break & 모든 패킷을 다 검사하게 되면 break (i는 인덱스!(길이-1))
        if endRange <= packetStart[i]:
            if littleCount == 1:
                count += 1
            startRange = endRange
            endRange = endRange + tau
            littleCount = 0
            i -= 1 # 하나의 패킷도 빠지지 않고, 해당하는 슬롯이 어디인지 찾을 때까지 반복

        elif startRange <= packetStart[i] < endRange:
            littleCount += 1

        i += 1

    return count


def pureALOHA(lamda, taus):
    Gs = []
    Ss = []
    idealSs = []

    for tau in taus:
        packetStart, packetEnd = packetGenerator(sample, lamda, tau)
        T = packetEnd[len(packetEnd) - 1]  # packetEnd 의 마지막 값

        # REAL
        # G = ( sample # / T ) * tau
        G = (sample / T) * tau
        S = (collisionCheckPureALOHA(sample, packetStart, packetEnd) / T) * tau

        # IDEAL
        idealG = tau
        idealS = idealG * math.exp(-2 * idealG)

        Gs.append(G)
        Ss.append(S)
        idealSs.append(idealS)

    return Gs, Ss, idealSs


def slottedALOHA(lamda, taus):
    Gs = []
    Ss = []
    idealSs = []

    for tau in taus:
        packetStart, packetEnd = packetGenerator(sample, lamda, tau)
        T = packetEnd[len(packetEnd) - 1]

        #REAL
        G = (sample / T) * tau
        S = (collisionCheckSlottedALOHA(sample, packetStart, packetEnd, tau, T) / T) * tau

        #IDEAL
        idealG = tau
        idealS = idealG * math.exp(-1 * idealG)

        Gs.append(G)
        Ss.append(S)
        idealSs.append(idealS)

    return Gs, Ss, idealSs


def drawGraph(xscale1, yscale1, idealscale1, xscale2, yscale2, idealscale2):
    plt.subplot(121)
    plt.plot(xscale1, yscale1, label='REAL')
    plt.plot(xscale1, idealscale1, 'r:', label='IDEAL')
    plt.legend(loc='right', frameon=False)
    plt.title('Pure ALOHA')
    plt.xlabel('G (attempts per packet time)')
    plt.ylabel('S (successful transmissions per packet time)')

    plt.subplot(122)
    plt.plot(xscale2, yscale2, label='REAL')
    plt.plot(xscale2, idealscale2, 'r:', label='IDEAL')
    plt.legend(loc='right', frameon=False)
    plt.title('Slotted ALOHA')
    plt.xlabel('G (attempts per packet time)')
    plt.ylabel('S (successful transmissions per packet time)')

    plt.show()


def main():
    lamda = 1
    taus = [ x * 0.1 for x in range(1, 30) ]


    pureG, pureS, pureIdealS = pureALOHA(lamda, taus)
    print("PURE COMPLETED")

    slottedG, slottedS, slottedIdealS = slottedALOHA(lamda, taus)
    print("SLOTTED COMPLETED")

    drawGraph(pureG, pureS, pureIdealS, slottedG, slottedS, slottedIdealS)


if __name__ == '__main__':
    main()
