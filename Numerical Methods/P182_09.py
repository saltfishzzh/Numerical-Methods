import numpy as np

X = [0.52, 3.1, 8.0, 17.95, 28.65, 39.62, 50.65, 78, 104.6, 156.6, 208.6, 260.7, 312.5,
     364.4, 416.3, 468, 494, 507, 520]
Y = [5.28794, 9.4, 13.84, 20.2, 24.9, 28.44, 31.1, 35, 36.5, 36.6, 34.6, 31.0, 26.34,
     20.9, 14.8, 7.8, 3.7, 1.5, 0.2]

Y0d = 1.86548
Y18d = -0.046115

XX = [2, 4, 6, 12, 16, 30, 60, 110, 180, 280, 400, 515]

N = len(X)


def calculateH(x):
    return [x[i] - x[i - 1] for i in range(1, N)]


def calculateU(h):
    return [h[i - 1] / (h[i] + h[i - 1]) for i in range(1, N - 1)]


def calculateL(miu):
    return [1 - miu[i] for i in range(len(miu))]


def calculateG(h, y):
    ret = [6 / (h[i] + h[i - 1]) * ((y[i + 1] - y[i]) / h[i] - (y[i] - y[i - 1]) / h[i - 1])
           for i in range(1, len(y) - 1)]
    ret.insert(0, 6 / h[0] * ((y[1] - y[0]) / h[0] - Y0d))
    ret.append(6 / h[-1] * (Y18d - (y[-1] - y[-2]) / h[-1]))
    return ret


def makeMatrix(miu, lambd):

    n = len(miu) + 2
    line_0 = [0 for x in range(n)]
    line_0[0] = 2
    line_0[1] = 1
    ret = [line_0]
    for i in range(1, n - 1):
        line_i = [0 for x in range(n)]
        line_i[i] = 2
        line_i[i - 1] = miu[i - 1]
        line_i[i + 1] = lambd[i - 1]
        ret.append(line_i)
    line_final = [0 for x in range(n)]
    line_final[-1] = 2
    line_final[-2] = 1
    ret.append(line_final)
    return ret


def makeFunctions(m, x, h, y):
    ret = []
    n = len(h)
    for i in range(n):
        ret.append(lambda k: (m[i] * (x[i + 1] - k) ** 3 / 6 / h[i] +
                              m[i + 1] * (k - x[i]) ** 3 / 6 / h[i] +
                              (y[i] - m[i] / 6 * h[i] * h[i]) / h[i] * (x[i + 1] - k) +
                              (y[i + 1] - m[i + 1] / 6 * h[i] * h[i]) / h[i] * (k - x[i])
                              ))
    return ret


def main():

    h = calculateH(X)

    u = calculateU(h)

    lambd = calculateL(u)

    g = calculateG(h, Y)

    res = makeMatrix(u, lambd)

    m = np.linalg.solve(res, g)

    funcs = makeFunctions(m, X, h, Y)

    for k in XX:
        for index, j in enumerate(X):
            if k > j:
                pass
            else:
                print(funcs[index - 1](k))
                break


if __name__ == '__main__':
    main()