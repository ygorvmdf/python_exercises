from node import Node


class Queue:
    def __init__(self):
        self.length = 0
        self.head = None

    def isEmpty(self):
        return self.length == 0

    def insert(self, cargo):
        import node
        node = Node(cargo)
        node.next = None
        if self.head is None:
            # if the list is empty the new node goes first
            self.head = node
        else:
            # find the last node in the list
            last = self.head
            while last.next: last = last.next
            # append the new node
            last.next = node
        self.length += 1

    def remove(self):
        cargo = self.head.cargo
        self.head = self.head.next
        return cargo


class ImprovedQueue:
    def __init__(self):
        self.length = 0
        self.head = None
        self.last = None

    def isEmpty(self):
        return self.length == 0

    def insert(self, cargo):
        node = Node(cargo)
        node.next = None
        if self.length == 0:
            # if list is empty, the new node is head and last
            self.head = self.last = node
        else:
            # find the last node
            last = self.last
            # append the new node
            last.next = node
            self.last = node
        self.length += 1

    def remove(self):
        cargo = self.head.cargo
        self.head = self.head.next
        self.length -= 1
        if self.length == 0:
            self.last = None
        return cargo


class PriorityQueue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def insert(self, item):
        self.items.append(item)

    def remove(self):
        maxi = 0
        for i in range(1, len(self.items)):
            if self.items[i] > self.items[maxi]:
                maxi = i
        item = self.items[maxi]
        self.items[maxi:maxi+1] = []
        return item


class Golfer:
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def __str__(self):
        return f'{self.name:<16}: {self.score}'

    def __cpm__(self, other):
        if self.score < other.score: return 1
        if self.score > other.score: return -1
        return 0


tiger = Golfer("Tiger Woods", 61)
phil = Golfer("Phil Mickelson", 72)
hal = Golfer("Hal Sutton", 69)

pq = PriorityQueue()
pq.insert(tiger)
pq.insert(phil)
pq.insert(hal)
while not pq.isEmpty(): print(pq.remove())