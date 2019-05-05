class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def serialise(node):
    resultString = ""
    stackList = []

    stackList.append(node)
    while len(stackList) > 0:
        if stackList[0] == ".":
            resultString += "@"+"-"
            # using @ as null delimiter
        else:
            resultString += stackList[0].val + "-"
            if stackList[0].left is not None:
                stackList.append(stackList[0].left)
            else:
                stackList.append(".")

            if stackList[0].right is not None:
                stackList.append(stackList[0].right)
            else:
                stackList.append(".")

        stackList.pop(0)

    return resultString


def helpfunc(node, valString):

    if len(valString) > 0:
        if valString[0] != "@":
            node.left = Node(valString[0])
        valString.pop(0)

        if valString[0] != "@":
            node.right = Node(valString[0])
        valString.pop(0)

        if node.left is not None:
            helpfunc(node.left, valString)
        if node.right is not None:
            helpfunc(node.right, valString)


def deserialise(string):
    valueList = string.split("-")

    node = Node(valueList[0])
    valueList.pop(0)

    temp = node

    helpfunc(node, valueList)

    return temp


node = Node('root', Node('left', Node('left.left')), Node('right'))

if deserialise(serialise(node)).left.left.val == 'left.left':
    print("Success")
else:
    print("Fail")
