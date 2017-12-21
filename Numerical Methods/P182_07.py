import numpy
from numpy import matrix

def Jacobi(A, b, x0, precision):
    L = numpy.triu(A, 1) * -1
    U = numpy.tril(A, -1) * -1
    D = matrix(numpy.diag(numpy.diag(A)))
    Bj = D.I * (L + U)
    fj = D.I.dot(b)
    x1 = Bj.dot(x0) + fj
    count = 1
    while (x1 - x0).max() > precision:
        count += 1
        x0 = x1
        x1 = Bj * x0 + fj

    return x1, count


def GaussSeidel(A, b, x0, precision):
    L = numpy.triu(A, 1) * -1
    U = numpy.tril(A, -1) * -1
    D = matrix(numpy.diag(numpy.diag(A)))
    Bg = (D - L).I.dot(U)
    fg = (D - L).I.dot(b)
    x1 = Bg.dot(x0) + fg
    count = 1
    while (x1 - x0).max() > precision:
        count += 1
        x0 = x1
        x1 = Bg.dot(x0) + fg
    return x1, count


def SOR(A, b, x0, precision, w):
    L = numpy.triu(A, 1) * -1
    U = numpy.tril(A, -1) * -1
    D = matrix(numpy.diag(numpy.diag(A)))
    Bw = (D - L.dot(w)).I.dot(D.dot(1 - w) + U.dot(w))
    fw = (D - L.dot(w)).I.dot(b).dot(w)
    x1 = Bw.dot(x0) + fw
    count = 1
    while abs((x1 - x0).max()) > precision:
        count += 1
        x0 = x1
        x1 = Bw.dot(x0) + fw
    return x1, count


def main():
    A = matrix([[4, -1, 0, -1, 0, 0],
                [-1, 4, -1, 0, -1, 0],
                [0, -1, 4, -1, 0, -1],
                [-1, 0, -1, 4, -1, 0],
                [0, -1, 0, -1, 4, -1],
                [0, 0, -1, 0, -1, 4]])

    b = matrix([0, 5, -2, 5, -2, 6]).T

    begin = matrix([0, 0, 0, 0, 0, 0]).T

    precision = 0.0001
    #Parameters

    JacobiResult = Jacobi(A, b, begin, precision)
    GaussSeideResult = GaussSeidel(A, b, begin, precision)
    SORResult1 = SOR(A, b, begin, precision, 1.334)
    SORResult2 = SOR(A, b, begin, precision, 1.95)
    SORResult3 = SOR(A, b, begin, precision, 0.95)
    #Calculate

    print('Jacobi:',JacobiResult[0])
    print('Iteration times:', JacobiResult[1])

    print('Gauss_Seidel:', GaussSeideResult[0])
    print('Iteration times:', GaussSeideResult[1])

    print('SOR: 1.334', SORResult1[0])
    print('Iteration times', SORResult1[1])

    print('SOR: 1.95', SORResult2[0])
    print('Iteration times', SORResult2[1])

    print('SOR: 0.95', SORResult3[0])
    print('Iteration times', SORResult3[1])
    #Print results

if __name__ == '__main__':
    main()
