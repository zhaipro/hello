# coding: utf-8
# http://www.matrix67.com/data/InvSqrt.pdf
import math
import struct


def change_format(ifmt, ofmt, a):
    a = struct.pack(ifmt, a)
    a = struct.unpack(ofmt, a)
    return a[0]


def q_rsqrt(number):
    threehalfs = 1.5

    x2 = number * 0.5
    y = number
    i = change_format('f', 'l', y)
    # evil floating point bit level hacking
    i = 0x5f3759df - (i >> 1)           # what the fuck?
    y = change_format('l', 'f', i)
    y = y * (threehalfs - x2 * y * y)   # 1st iteration
    y = y * (threehalfs - x2 * y * y)   # 2nd iteration, this can be removed
    return y


if __name__ == '__main__':
    a = 2
    print(q_rsqrt(a))
    print(1 / math.sqrt(a))
