#  MIT (c) jtankersley 2019-05-18


class DoubleNode():
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def __str__(self):
        return f"{data}"


class DoubleList():
    def __init__(self):
        self.head = None
        self.tail = None

    def __str__(self):
        string = ""
        if self.head:
            string += str(self.head)
        # node = self.head.data
        # if node.right:
        #     string += self.__str__()
        # while node:
        #     string += f"{node.data},"
        #     node = node.right
        # print(f"{string}")
        print(f"__str__()={self.head.data}")
        return string

    def addHead(self, data):
        if self.head:
            self.head = DoubleNode(data, None, self.head)
            self.head.right.left = self.head
