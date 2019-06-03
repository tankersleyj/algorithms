#  MIT (c) jtankersley 2019-05-18


class BinaryNode():
    def __init__(self, data=None, parent=None, childLeft=None, childRight=None):
        self.data = data
        self.parent = parent
        self.childLeft = childLeft
        self.childRight = childRight

    def __str__(self):
        return f"{self.data}"


class BinaryTree():
    def __init__(self):
        self.head = None

    def __str__(self):
        string = ""
        # if self.head:
        #     node = self.head
        #     while node:
        #         string += f"{str(node.data)},"
        #         node = node.right
        return string[:len(string) -1] if len(string) > 0 else ""

    def add(self, data):
        if self.head:
            self.head = BinaryNode(data, self.head)
        else:
            self.head = BinaryNode(data)

    def remove(self, data):
        if self.head:
            self.head = BinaryNode(data, self.head)
        else:
            self.head = BinaryNode(data)

    def getInOrderList(self):
        return []
