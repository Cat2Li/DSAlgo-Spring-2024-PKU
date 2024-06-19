from __future__ import annotations
from numbers import Number


class Fraction(object):

    @staticmethod
    def sgn(num: Number):
        if num > 0:
            return 1
        elif num < 0:
            return -1
        else:
            return 0

    @staticmethod
    def gcd(a: int, b: int):
        while b:
            a, b = b, a % b
        return a

    def __init__(self, num: int, den: int):
        assert isinstance(num, int)
        assert isinstance(den, int)

        self.sign = self.sgn(num) * self.sgn(den)

        self.num = abs(num)
        self.den = abs(den)

        if self.num == 0:
            self.den = 1
        else:
            g = self.gcd(self.num, self.den)
            self.num //= g
            self.den //= g

    def __str__(self):
        return str(self.sign * self.num) + '/' + str(self.den)

    def __add__(self, other: Fraction):
        return Fraction(
            self.sign * self.num * other.den +
            other.sign * other.num * self.den, self.den * other.den)

    def __sub__(self, other: Fraction):
        return Fraction(
            self.sign * self.num * other.den -
            other.sign * other.num * self.den, self.den * other.den)

    def __mul__(self, other: Fraction):
        return Fraction(self.sign * other.sign * self.num * other.num,
                        self.den * other.den)

    def __div__(self, other: Fraction):
        return Fraction(self.sign * other.sign * self.num * other.den,
                        self.den * other.num)

    def __eq__(self, other: Fraction):
        return self.sign * self.num * other.den == other.sign * other.num * self.den


num_1, den_1, num_2, den_2 = map(int, input().split())
f1 = Fraction(num_1, den_1)
f2 = Fraction(num_2, den_2)
print(f1 + f2)
