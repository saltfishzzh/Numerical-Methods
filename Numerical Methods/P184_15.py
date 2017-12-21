import math

A = 0
B = math.pi / 2


def f(x):
    return (1 - 3.0 / 4 * (math.sin(x)**2))**0.5


def trapezoidal(n):
    h = (B - A) / n
    return h / 2 * (f(A) + 2 * sum(map(f, [A + (B - A) / n * k for k in range(1, n)])) + f(B))


def simpson(n):
    return 4.0 / 3 * trapezoidal(2 * n) - 1 / 3 * trapezoidal(n)


def newton(n):
    return 16.0 / 15 * simpson(2 * n) - 1 / 15 * trapezoidal(n)


def romberg(n):
    return 64.0 / 63 * newton(2 * n) - 1 / 63 * newton(n)


def main():
    for i in range(4):
        print(romberg(i + 1) * 4 * 20)


if __name__ == '__main__':
    main()
