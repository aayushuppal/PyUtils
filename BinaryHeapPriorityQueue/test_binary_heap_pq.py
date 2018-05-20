import unittest
from binary_heap_pq import BinaryHeapPriorityQueue

class TestNode(object):
    def __init__(self, val):
        self.val = val

class TestLocal(unittest.TestCase):

    def test_node1(self):

        A = BinaryHeapPriorityQueue( prefer=(lambda lhs, rhs :
                                     lhs if lhs.val >= rhs.val else rhs)
                                   , size=5)
        A.add(TestNode(1))
        A.add(TestNode(4))
        A.add(TestNode(3))
        A.add(TestNode(5))
        A.add(TestNode(2))

        self.assertEqual(5, A.pop().val)
        self.assertEqual(4, A.pop().val)
        self.assertEqual(3, A.pop().val)
        self.assertEqual(2, A.pop().val)
        self.assertEqual(1, A.pop().val)

    def test_node2(self):

        A = BinaryHeapPriorityQueue( prefer=(lambda lhs, rhs :
                                     lhs if lhs.val <= rhs.val else rhs)
                                   , size=3)
        A.add(TestNode(1))
        A.add(TestNode(4))
        A.add(TestNode(3))

        self.assertEqual(1, A.pop().val)
        self.assertEqual(3, A.pop().val)
        self.assertEqual(4, A.pop().val)

    def test_val1(self):

        A = BinaryHeapPriorityQueue( prefer=(lambda lhs, rhs :
                                     lhs if lhs >= rhs else rhs)
                                   , size=3)
        A.add(1)
        A.add(3)
        A.add(2)

        self.assertEqual(3, A.pop())
        self.assertEqual(2, A.pop())
        self.assertEqual(1, A.pop())
        self.assertEqual(None, A.pop())
        self.assertEqual(0, A.size())

# =============================================================================
if __name__ == "__main__":
    unittest.main()
