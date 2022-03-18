import math
import matplotlib.pyplot as plt


PI = math.pi
SCALE = 301


def calcAlpha():
    return PI / 4


def calcBetaN(n, N0):
    return (PI * n) / N0


def calcFn(Fd, n, N):
    return Fd * math.cos((2*PI*n) / N)


def calcFd(v, Fc):
    return v / (1/Fc)


def calcCarrier(Fn,t):
    return math.cos(2*PI*Fn*t)


def calcRealPart(Bn): # 2cos(Bn)
    return 2*math.cos(Bn)


def calcImaginaryPart(Bn): # 2sin(Bn)
    return 2*math.sin(Bn)


def main():
    # 초기 설정
    t = [ x for x in range(SCALE) ]

    v = 3
    Fc = 800 * (10**6)
    N0 = 16 # 16개의 파형

    Fd = calcFd(v, Fc)
    N = (4 * N0) + 2


    # Xr(t) 와 Xi(t) 계산
    Xr = [ 0 for x in range(len(t)) ]
    Xi = [ 0 for x in range(len(t)) ]

    for i in t: # 각 시간에 대한 값을 계산
        for n in range(1, N0+1):
            Bn = calcBetaN(n, N0)
            Fn = calcFn(Fd, n, N)

            real = calcRealPart(Bn)
            imagine = calcImaginaryPart(Bn)

            carrier = calcCarrier(Fn, i)

            # 해당 시간에 각각의 펄스 값을 누적
            Xr[i] += real * carrier
            Xi[i] += imagine * carrier
            pass

        # 마지막 루트 1/2 더해줌 | calcAlpha = PI / 4
        Xr[i] += ( 2*math.cos(calcAlpha()) ) * ( (1/math.sqrt(2)) * math.cos(2*PI*Fd*i) )
        Xi[i] += ( 2*math.sin(calcAlpha()) ) * ( (1/math.sqrt(2)) * math.cos(2*PI*Fd*i) )
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
    # !!!!!로그 스케일로 출력 해야함!!!!!
    # 일단 기본으로 해보고 (OK) 로그로 바꿔보자
    print("Size of T :",len(t))
    print("Size of X2:", len(X2))  #사이즈 동일

    # plt.plot(t, X2)
    plt.plot(t, Xlog)# LOG 스케일 출력
    plt.xlabel('t')
    plt.ylabel('log10(|X(t)|^2)')
    plt.title('Jakes Model - Suggested Model')
    plt.show()


    # 각 변수 별 값 확인 (대략적으로)
    # for m in range(10):
    #     for n in range(10):
    #         print("%.3f"%(Xr[10*m+n]), end='   ')
    #     print()
    #
    # print('\n\n')
    #
    # for m in range(10):
    #     for n in range(10):
    #         print("%.3f"%(Xi[10*m+n]), end='   ')
    #     print()
    # print('\n\n')
    # for m in range(10):
    #     for n in range(10):
    #         print("%.3f"%(X[10*m+n]), end='   ')
    #     print()
    # print('\n\n')
    # for m in range(10):
    #     for n in range(10):
    #         print("%.3f"%(X2[10*m+n]), end='   ')
    #     print()


if __name__ == "__main__":
    main()