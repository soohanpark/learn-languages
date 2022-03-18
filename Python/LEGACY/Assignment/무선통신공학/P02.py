import math
import matplotlib.pyplot as plt
import random


PI = math.pi
SCALE = 301
# 난수 생성
randomDict = []
i=0
while i < 2*PI*100:
    randomDict.append(i/100)
    i += 1


def calcAlphaN():
    return random.choice(randomDict)


def calcAN():
    return random.choice(randomDict)


def calcBN():
    return random.choice(randomDict)


def calcFd(v, Fc):
    return v / (1/Fc)


def calcRealPart(Fd, Alpha, t, An): # cos(2*pi*Fd*cos(Alpha*t)+An)
    return math.cos((2 * PI * Fd * math.cos(Alpha * t)) + An)


def calcImaginaryPart(Fd, Alpha, t, Bn): # sin(2*pi*Fd*cos(Alpha*t)+An)
    return math.sin((2 * PI * Fd * math.cos(Alpha * t)) + Bn)


def main():
    # 초기 설정
    t = [ x for x in range(SCALE) ]

    v = 60
    Fc = 3500 * (10**6)
    N0 = 16 # 16개의 파형

    Fd = calcFd(v, Fc)
    N = (4 * N0) + 2


    # Xr(t) 와 Xi(t)를 각 시간에 대한 값을 계산
    Xr = [ 0 for x in range(len(t)) ]
    Xi = [ 0 for x in range(len(t)) ]

    for i in t:
        for n in range(1, N0+1):
            Alpha = calcAlphaN()
            An = calcAN()
            Bn = calcBN()

            real = calcRealPart(Fd, Alpha, i, An)
            imagine = calcImaginaryPart(Fd, Alpha, i, Bn)

            # 해당 시간에 각각의 펄스 값을 누적
            Xr[i] += real
            Xi[i] += imagine
            pass

        # 마지막 루트 1/N 곱해줌
        Altitude = 1 / math.sqrt(N)
        Xr[i] *= Altitude
        Xi[i] *= Altitude
        pass


    # |X(t)| 계산
    X = []
    for i in t:
        X.append(math.sqrt( math.pow(Xr[i], 2) + math.pow(Xi[i], 2) ))


    # |X(t)|^2 계산
    X2 = [ X[i]*X[i] for i in range(len(X)) ]


    # X2 로그 스케일로 변환
    Xlog = [ math.log10(X2[i]) for i in range(len(X2)) ]


    # 그래프 그리기 | x축: t , y축: log10(X2)
    plt.plot(t, Xlog)
    plt.xlabel('t')
    plt.ylabel('log10(|X(t)|^2)')
    plt.title('Jakes Model - Scattering Model')
    plt.show()


if __name__ == "__main__":
    main()