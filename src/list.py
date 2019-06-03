#  MIT (c) jtankersley 2019-05-18


class DoubleLinkNode():
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def __str__(self):
        """Print data ."""
        return f"{self.data}"


class DoubleLinkList():
    def __init__(self):
        self.head = None
        self.tail = None

    def __str__(self):
        """Print data as comma delimited list."""
        string = ""
        if self.head:
            node = self.head
            while node:
                string += f"{str(node.data)},"
                node = node.right
        return string[:len(string) -1] if len(string) > 0 else ""

    def add_head(self, data):
        if self.head:
            self.head = DoubleLinkNode(data, None, self.head)
            self.head.right.left = self.head
        else:
            self.head = DoubleLinkNode(data)
            self.tail = self.head

    def peak_head(self):
        if self.head:
            return self.head.data

    def pop_head(self):
        if self.head:
            node = self.head
            if self.head.right:
                self.head = self.head.right
                self.head.left = None
            return node.data

    def add_tail(self, data):
        if self.tail:
            self.tail.right = DoubleLinkNode(data, self.tail, None)
            self.tail = self.tail.right
        else:
            self.head = DoubleLinkNode(data)
            self.tail = self.head

    def peek_tail(self):
        if self.tail:
            return self.tail.data

    def pop_tail(self):
        if self.tail:
            node = self.tail
            if self.tail.left:
                self.tail = self.tail.left
                self.tail.right = None
            return node.data
