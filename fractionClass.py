class Fraction:
    def __init__(self, numerator, denominator=1):
        g = gcd(numerator, denominator)
        self.numerator = numerator / g
        self.denominator = denominator / g

    def __str__(self):
        return f"{self.numerator}/{self.denominator}"

    def __mul__(self, other):
        if isinstance(other, int):
            other = Fraction(other)
        return Fraction(self.numerator*other.numerator, self.denominator*other.denominator)

    __rmul__ = __mul__

    def __add__(self, other):
        if isinstance(other, int):
            other = Fraction(other)
        return Fraction(self.numerator * other.denominator +
                        self.denominator * other.numerator,
                        self.denominator * other.denominator)

    __radd__ = __add__

    def __cmp__(self, other):
        diff = (self.numerator * other.denominator -
                other.numerator * self.denominator)
        return diff

    def __sub__(self, other):
        if isinstance(other, int):
            other = Fraction(other)
        return Fraction(self.numerator * other.denominator -
                        self.denominator * other.numerator,
                        self.denominator * other.denominator)

    def __div__(self, other):
        if isinstance(other, int):
            other = Fraction(other)
        return Fraction(self.numerator * other.denominator,
                        self.denominator * other.numerator)

    def __pow__(self, other):
        if isinstance(other, int):
            other = Fraction(other)
        result = Fraction(self.numerator ** (other.numerator / other.denominator),
                          self.denominator ** (other.numerator / other.denominator))


def gcd(m, n):
    if m % n == 0:
        return n
    else:
        return gcd(n, m % n)
