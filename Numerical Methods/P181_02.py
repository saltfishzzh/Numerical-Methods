#3150102418 Numerical Methods P181_2

import math

def dichotomy(f, x, y, precision, count):
    m = (x + y) / 2.0
    a = f(x)
    b = f(y)
    c = f(m)

    if (a < 0 and b < 0) or (a > 0 and b > 0):
        return (-1, -1)

    if abs(x - m) > precision:
        if (a > 0 and c < 0) or (a < 0 and c > 0):
            return dichotomy(f, x, m, precision, count + 1)
        else:
            return dichotomy(f, m, y, precision, count + 1)
    else:
        return (m, count)


def iteration(g, x0, precision, L, count):
    x, x_next = x0, g(x0)
    while abs(x - x_next) / (1.0 - L) > precision:
        x = x_next
        x_next = g(x)
        count += 1
    return (x_next, count)

def newton(f, derivative, x0, precision, count):
    def n(x):
        return x - f(x)/derivative(x)

    x, x_next = x0, n(x0)
    while abs(x - x_next) > precision:
        x, x_next = x_next, n(x_next)
        count += 1
    return (x_next, count)

def f(x):
    return math.exp(x) + 10 * x - 2

def g(x):
    return (2 - math.exp(x)) / 10

def h(x):
    return math.exp(x) + 10

def main():
    precision = 0.0005

    a = dichotomy(f, 0, 1, precision, 1)
    print("dichotomy:")

    if a[1] == -1:
        print("Error!")
    else:
        print(a)

    b = iteration(g, 0, precision, math.e / 10, 1)
    print("iteration:")
    print(b)

    c = newton(f, h, 0, precision, 1)
    print("newton:")
    print(c)


if __name__ == '__main__':
    main()
