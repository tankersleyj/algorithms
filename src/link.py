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
        if self.head:
            node = self.head
            while node:
                string += f"{str(node.data)},"
                node = node.right
            return string[:len(string) -1] if len(string) > 0 else ""
        if self.tail:
            node = self.tail
            while node:
                string = f"{str(node.data)},{string}"
                node = node.left
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

    def addTail(self, data):
        if self.tail:
            self.tail.right = DoubleNode(data, self.tail, None)
            self.tail = self.tail.right
        else:
            self.tail = DoubleNode(data)

    def peekTail(self):
        if self.tail:
            return self.tail.data

    def popTail(self):
        if self.tail:
            node = self.tail
            if self.tail.left:
                self.tail = self.tail.left
                self.tail.right = None
            return node.data

    # def addTail(self, data):
    #     if self.tail:
    #         self.tail = DoubleNode(data, self.head)
    #         self.head.right.left = self.head
    #     else:
    #         self.tail = DoubleNode(data)
    #         self.head = self.tail
