class Tree:
    def __init__(self, cargo, left=None, right=None):
        self.cargo = cargo
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.cargo)


left = Tree(2)
right = Tree(3)
tree = Tree('+', Tree(1), Tree('*', Tree(2), Tree(3)))


def total(tree):
    if tree is None: return 0
    return total(tree.left) + total(tree.right) + tree.cargo


def printTreePostorder(tree):
    if tree is None: return
    printTreePostorder(tree.left)
    printTreePostorder(tree.right)
    print(tree.cargo)


def printTreeInorder(tree):
    if tree is None: return
    if tree.left is not None and tree.right is not None:
        print('(', end=' ')
        printTreeInorder(tree.left)
        print(tree.cargo, end=' ')
        printTreeInorder(tree.right)
        print(')', end=' ')
    else:
        print(tree.cargo, end=' ')


def printTreeIndented(tree, level=0):
    if tree is None: return
    printTreeIndented(tree.right, level+1)
    print(' ' * level + str(tree.cargo))
    printTreeIndented(tree.left, level+1)


def getToken(tokenlist, expected):
    if tokenlist[0] == expected:
        del tokenlist[0]
        return True
    else:
        return False


def getNumber(tokenList):
    if getToken(tokenList, '('):
        x = getSum(tokenList)
        if not getToken(tokenList, ')'):
            raise ValueError('missing parenthesis')
        return x
    else:
        x = tokenList[0]
        if not isinstance(x, int): return None
        del tokenList[0]
        return Tree(x, None, None)


def getProduct(tokenList):
    a = getNumber(tokenList)
    if getToken(tokenList, '*'):
        b = getProduct(tokenList)
        return Tree('*', a, b)
    else:
        return a


def getSum(tokenLista):
    a = getProduct(tokenList)
    if getToken(tokenList, '+'):
        b = getSum(tokenList)
        return Tree('+', a, b)
    else:
        return a


tokenList = [9, 11, 'end']
x = getNumber(tokenList)
printTreePostorder(x)
print(tokenList)
