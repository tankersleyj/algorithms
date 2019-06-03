# MIT (c) jtankersley 2019-05-19
import unittest
from src import tree
from src import timer


orderedList = [1,2,3,4,5,6,7,8,10,12,15,20,25,30,31,32]
unOrderedList = [10,20,31,4,6,5,15,2,12,25,3,30,32,1,7,8]
multiOrderedList = [1,2,3,3,3,3,4,5,6,7,7,8,10,12,12,12,15,20,25,30,31,32]
multiUnOrderedList = [10,20,12,31,3,4,12,6,5,15,7,3,2,12,25,3,3,30,32,1,7,8]


class TestSort(unittest.TestCase):

    def test_BinaryTree(self):
        bt = tree.BinaryTree()
        for n in unOrderedList:
            bt.add(n)
        actual = bt.getInOrderList()
        expected = orderedList
        self.assertEqual(actual, expected, "test_binaryTree.1")

    def test_BinaryTree(self):
        bt = tree.BinaryTree()
        for n in multiUnOrderedList:
            bt.add(n)
        actual = bt.getInOrderList()
        expected = orderedList
        self.assertEqual(actual, expected, "test_binaryTree.2")

    def test_multiBinaryTree(self):
        mbt = tree.MultiBinaryTree()
        for n in multiUnOrderedList:
            mbt.add(n)
        actual = mbt.getInOrderList()
        expected = multiOrderedList
        self.assertEqual(actual, expected, "test_multiBinaryTree")
