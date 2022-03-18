import math
from matplotlib import pyplot as plt


def setInitState(bits):
    bits = str(bits)
    reg = dict()
    i = 1
    for b in bits:
        reg[i] = int(b)
        i += 1

    return reg


def generator(reg, N):
    output = []
    for n in range(N*3):
        if reg[4] == 0:
            output.append(-1)
        else:
            output.append(reg[4])
        if reg[3] != reg[4]:
            temp = 1
        else:
            temp = 0
        reg[4] = reg[3]
        reg[3] = reg[2]
        reg[2] = reg[1]
        reg[1] = temp

    return output


def makeAutoCorr(output, K, N):
    autoCorr = []
    for k in K:
        temp = 0
        for n in range(N):
            temp += output[n] * output[n+k]

        autoCorr.append((1/N) * temp)

    return autoCorr


def makeGraph(k, autoCorr):
    plt.plot(k, autoCorr)
    plt.title('Auto-correlation of m-sequence')
    plt.show()


def main():
    m = 4  # num of registers
    N = (2 ** m) - 1 # 15

    reg = setInitState(1111) # set state
    output = generator(reg, N)

    k = [ x for x in range(-20, 21) ]
    autoCorr = makeAutoCorr(output, k, N)

    makeGraph(k, autoCorr)


if __name__ == '__main__':
    main()