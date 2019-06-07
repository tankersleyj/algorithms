# MIT (c) jtankersley 2019-06-04
import unittest
from src import heapq
from src import timer


multiUnOrderedDictList = [
    (31,"u"),(3,"e"),(2,"b"),(4,"g"),(32,"v"),(7,"j"),(1,"a"),(20,"r"),(7,"k"),(3,"d"),(15,"q"),
    (10,"m"),(8,"l"),(3,"f"),(12,"n"),(12,"o"),(5,"h"),(6,"i"),(12,"p"),(25,"s"),(3,"c"),(30,"t")]
multiOrderedDictList = [
    (1,"a"),(2,"b"),(3,"c"),(3,"d"),(3,"e"),(3,"f"),(4,"g"),(5,"h"),(6,"i"),(7,"j"),(7,"k"),(8,"l"),
    (10,"m"),(12,"n"),(12,"o"),(12,"p"),(15,"q"),(20,"r"),(25,"s"),(30,"t"),(31,"u"),(32,"v")]
multiOrderedDictReverseList = [
    (32,"v"),(31,"u"),(30,"t"),(25,"s"),(20,"r"),(15,"q"),(12,"p"),(12,"o"),(12,"n"),(10,"m"),(8,"l"),
    (7,"k"),(7,"j"),(6,"i"),(5,"h"),(4,"g"),(3,"f"),(3,"e"),(3,"d"),(3,"c"),(2,"b"),(1,"a")]


class TestHeap(unittest.TestCase):

    def test_HeapQPriorityPop(self):
        mh = heapq.HeapQ(multiUnOrderedDictList)  # push list elements onto heap
        print(f"mh.HeapQPop.str={str(mh)}")
        actual = []
        while not mh.is_empty():
            actual.append(mh.pop())
        expected = multiOrderedDictList
        print(f"HeapQPop.actual={actual}")
        print(f"HeapQPop.expected={expected}")
        self.assertEqual(actual, expected, "test_HeapQPop")
