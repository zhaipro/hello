# coding: utf-8
import math


def _sqrt(x, a):
    '''
    f(x) = x ^ 2 - a = 0
    f(x) / f'(x) = 0
    x - f(x) / f'(x) = x
    x - (x ^ 2 - a) / (2x) = x
    x = (x + a / x) / 2
    '''
    return (x + a / x) / 2


def sqrt(a, iters=4):
    x = 1
    for _ in range(iters):
        x = _sqrt(x, a)
    return x


def _cubic(x, a, b, c):
    return (3 * a * x * x - b * x - c) / (6 * a * x + b)


def convex(a, b, c, iters=4, x=0):
    for _ in range(iters):
        x = _cubic(x, a, b, c)
    return x


if __name__ == '__main__':
    for a in range(1, 100):
        diff = math.sqrt(a) - sqrt(a, 7)
        assert abs(diff) < 0.0000001, a
    a, b, c = 1, 3, -6
    x = convex(a, b, c, iters=20)
    assert abs(3 * a * x ** 2 + 2 * b * x + c) < 0.0000001, x
    print("Hello Newton's method!")
