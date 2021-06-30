class Time:
    """
    Creates an object that take the current hours.
    """

    def __init__(self, h=0, m=0, s=0):
        self.hours = h
        self.minutes = m
        self.seconds = s

    def printTime(self):
        print(str(self.hours) + ':' +
              str(self.minutes) + ':' +
              str(self.seconds))

    def increment(self, seconds):
        self.seconds += seconds
        if seconds >= 60:
            n = seconds // 60
            self.seconds -= 60 * n
            self.minutes += 1 * n
        if self.minutes >= 60:
            n = self.minutes // 60
            self.minutes -= 60 * n
            self.hours += 1 * n

    def convertToseconds(self):
        suma = (self.hours * 3600) + (self.minutes * 60) + self.seconds
        return suma


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return '(' + str(self.x) + ',' + str(self.y) + ')'

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)


def find(txt, ch, start=0, ends=0):
    index = start
    if ends == 0:
        ends = len(txt)
    while index < ends:
        if txt[index] == ch:
            return index
        index += 1
    return -1