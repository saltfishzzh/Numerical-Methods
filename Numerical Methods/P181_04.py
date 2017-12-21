from decimal import *


A = [[1.1348, 3.8326, 1.1651, 3.4017],
     [0.5301, 1.7875, 2.5330, 1.5435],
     [3.4129, 4.9317, 8.7643, 1.3142],
     [1.2371, 4.9998, 10.6721, 0.0147]]

B = [9.5342, 6.3941, 18.4231, 16.9237]

x = [0 for x in range(len(A))]



def gauss():

    n = len(A)
    for k in range(0, n-1):
        for i in range(k+1, n):
            m = round(A[i][k] / A[k][k], 4)
            A[i][k] = Decimal('0.000')
            for j in range(k+1, n):
                A[i][j] = round(A[i][j] - m*A[k][j], 4)
            B[i] = round(B[i] - m*B[k], 4)

    x[n-1] = round(B[n-1]/A[n-1][n-1], 4)
    for i in range(n-2, -1, -1):
        x[i] = round((B[i] - sum([A[i][j]*x[j] for j in range(i+1, n)]))/A[i][i], 4)


def column_main():

    n = len(A)
    for k in range(0, n-1):
        index_max = k
        for i in range(k, n):
            if A[i][k] > A[index_max][k]:
                index_max = i
        A[k], A[index_max] = A[index_max], A[k]
        B[k], B[index_max] = B[index_max], B[k]

        for i in range(k+1, n):
            m = round(A[i][k] / A[k][k], 4)
            for j in range(k+1, n):
                A[i][j] = round(A[i][j] - m*A[k][j], 4)
            B[i] = round(B[i] - m*B[k], 4)


    x[n-1] = round(B[n-1]/A[n-1][n-1], 4)
    for i in range(n-2, -1, -1):
        x[i] = round((B[i] - sum([A[i][j]*x[j] for j in range(i+1, n)]))/A[i][i], 4)




def main():

    for i, a in enumerate(A):
        for j, aa in enumerate(A):
            A[i][j] = Decimal(str(A[i][j]))

    for i, b in enumerate(B):
        B[i] = Decimal(str(B[i]))

    for i, xx in enumerate(x):
        x[i] = Decimal(str(x[i]))
    getcontext().rounding = ROUND_HALF_UP

    gauss()
    column_main()
    print(x)


if __name__ == '__main__':
    main()
