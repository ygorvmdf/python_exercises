class Node:
    def __init__(self, cargo=None, next=None):
        self.cargo = cargo
        self.next = next

    def __str__(self):
        return str(self.cargo)

    def printBackward(self):
        if self.next is not None:
            tail = self.next
            tail.printBackwards()
        print(self.cargo)


nodex = Node(5)
node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node1.next = node2
node2.next = node3


def printList(node):
    print('[', end='')
    while node:
        if node.next is None:
            print(node, end='')
            break
        print(node, end=', ')
        node = node.next
    print(']')


def printBackwards(list):
    if list is None: return
    head = list
    tail = list.next
    printBackwards(tail)
    print(head, end=' ')


def removeSecond(list):
    if list is None: return
    if list.next is None: return
    first = list
    second = list.next
    # make the first node refer to the third
    first.next = second.next
    # separate the second node from the rest of the list
    second.next = None
    return second


def printBackwardsNicely(list):
    print('[', end=' ')
    printBackwards(list)
    print(']')


class LinkedList:
    def __init__(self):
        self.length = 0
        self.head = None

    def printBackward(self):
        print('[', end='')
        if self.head is not None:
            self.head.printBackward()
        print(']', end='')

    def addFisrt(self, cargo):
        node = Node(cargo)
        node.next = self.head
        self.head = node
        self.length += 1
