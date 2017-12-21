
def f(x, y):
    return (2.0 * x) / (3.0 * y * y)

def Euler():
    print ('Euler:')
    yi = 1.0
    for i in range(0, 10):
        xi = i * 0.1
        yi = yi + 0.1 * f(xi, yi)
        print ('xi = ', round(xi, 2), 'yi+1 = ', yi, 'y = ', (1 + xi + 0.1) ** (1/3))

def Euler2():
    print ('Improved Euler:')
    yi = 1.0
    for i in range(0, 10):
        xi = i * 0.1
        t1 = yi + 0.1 * f(xi, yi)
        t2 = yi + 0.1 * f(xi + 0.1, t1)
        yi = 0.5 * (t1 + t2)
        print ('xi = ', round(xi, 2), 'yi+1 = ', yi, 'y = ', (1 + xi + 0.1) ** (1 / 3))

def R_K():
    print ('R-K:')
    yi = 1.0
    for i in range(0, 10):
        xi = i * 0.1
        k1 = f(xi, yi)
        k2 = f(xi + 0.05, yi + 0.05 * k1)
        k3 = f(xi + 0.05, yi + 0.05 * k2)
        k4 = f(xi + 0.1, yi + 0.1 * k3)
        yi = yi + (k1 + 2 * k2 + 2 * k3 + k4) / 60.0
        print ('xi = ', round(xi, 2), 'yi+1 = ', yi, 'y = ', (1 + xi + 0.1) ** (1 / 3))

def main():
    Euler()
    Euler2()
    R_K()


if __name__ == '__main__':
    main()



