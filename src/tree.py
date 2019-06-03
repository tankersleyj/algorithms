#  MIT (c) jtankersley 2019-05-18


class BinaryNode():
    # distinct value binary node

    def __init__(self, data=None, parent=None, childLeft=None, childRight=None):
        self.data = data
        self.parent = parent
        self.childLeft = childLeft
        self.childRight = childRight

    def __str__(self):
        return f"{self.data}"


class BinaryTree():
    # distinct value binary tree

    def __init__(self):
        self.root = None

    def __str__(self):
        return str(self.getInOrderList())

    def _add(self, data, node):
        if data < node.data:
            if node.childLeft:
                self._add(data, node.childLeft)
            else:
                node.childLeft = BinaryNode(data, node)
        if data > node.data:
            if node.childRight:
                self._add(data, node.childRight)
            else:
                node.childRight = BinaryNode(data, node)

    def add(self, data):
        if self.root:
            self._add(data, self.root)    
        else:
            self.root = BinaryNode(data)

    def _getInOrderList(self, node):
        if node:
            list = []
            if node.childLeft:
                leftList = self._getInOrderList(node.childLeft)
                list = [*list, *leftList]
            list = [*list, node.data]
            if node.childRight:
                rightList = self._getInOrderList(node.childRight)
                list = [*list, *rightList]
            return list
        else:
            return None        

    def getInOrderList(self):
        if self.root:
            return self._getInOrderList(self.root)
        else:
            return []

class MultiBinaryNode():
    # distinct value binary node

    def __init__(self, data=None, parent=None, childLeft=None, childRight=None):
        self.data = data
        self.dataCount = 1
        self.parent = parent
        self.childLeft = childLeft
        self.childRight = childRight

    def __str__(self):
        return f"{self.data}"


class MultiBinaryTree():
    # distinct value binary tree

    def __init__(self):
        self.root = None

    def __str__(self):
        return str(self.getInOrderList())

    def _add(self, data, node):
        if data == node.data:
            node.dataCount += 1
        elif data < node.data:
            if node.childLeft:
                self._add(data, node.childLeft)
            else:
                node.childLeft = MultiBinaryNode(data, node)
        elif data > node.data:
            if node.childRight:
                self._add(data, node.childRight)
            else:
                node.childRight = MultiBinaryNode(data, node)

    def add(self, data):
        if self.root:
            self._add(data, self.root)    
        else:
            self.root = MultiBinaryNode(data)

    def _getInOrderList(self, node):
        if node:
            list = []
            if node.childLeft:
                leftList = self._getInOrderList(node.childLeft)
                list = [*list, *leftList]
            for n in range(node.dataCount):
                list = [*list, node.data]
            if node.childRight:
                rightList = self._getInOrderList(node.childRight)
                list = [*list, *rightList]
            return list
        else:
            return None        

    def getInOrderList(self):
        if self.root:
            return self._getInOrderList(self.root)
        else:
            return []