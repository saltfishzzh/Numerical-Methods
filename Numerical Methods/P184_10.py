import numpy as np

X = [1, 3, 4, 5, 6, 7, 8, 9, 10]
Y = [10, 5, 4, 2, 1, 1, 2, 3, 4]

def main():
    a = []
    temp = [len(X)]
    for i in range(2):
        temp.append(sum(map(lambda x: x**(i + 1), X)))

    a.append(temp)
    temp1 = temp[1:]
    temp1.append(sum(map(lambda x: x**3, X)))
    a.append(temp1)
    temp1 = temp1[1:]
    temp1.append(sum(map(lambda x: x**4, X)))
    a.append(temp1)

    b = [sum(map(lambda x, y: x**i * y, X, Y)) for i in range(3)]

    x = np.linalg.solve(a, b)

    p = np.polynomial.Polynomial(x)

    print('y = ', x[0], x[1], 'x + ', x[2], 'x^2')

    print('(', -x[1]/2/x[2], p(-x[1]/2/x[2]), ')')


if __name__ == '__main__':
    main()
