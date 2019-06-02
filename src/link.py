#  MIT (c) jtankersley 2019-05-18


class DoubleNode():
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def __str__(self):
        return f"{self.data}"


class DoubleList():
    def __init__(self):
        self.head = None
        self.tail = None

    def __str__(self):
        string = ""
        node = self.head
        while node:
            string += f"{str(node.data)},"
            node = node.right
        return string[:len(string) -1] if len(string) > 0 else ""

    def addHead(self, data):
        if self.head:
            self.head = DoubleNode(data, None, self.head)
            self.head.right.left = self.head
        else:
            self.head = DoubleNode(data)

    def peekHead(self):
        if self.head:
            return self.head.data

    def popHead(self):
        if self.head:
            node = self.head
            if self.head.right:
                self.head = self.head.right
                self.head.left = None
            return node.data

    # def addTail(self, data):
    #     if self.tail:
    #         self.tail = DoubleNode(data, self.head)
    #         self.head.right.left = self.head
    #     else:
    #         self.tail = DoubleNode(data)
    #         self.head = self.tail
