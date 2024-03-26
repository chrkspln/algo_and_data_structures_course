import unittest
from src.AVLPriorityQueue import *


class TestPriorityQueue(unittest.TestCase):
    queue = PriorityQueue(4, 5)

    def test_insertion_and_deletion_normal_case(self):
        self.queue.enqueue(3, 3)
        self.queue.enqueue(7, 6)
        self.assertEqual(self.queue.avl_tree.root.value, 4)
        self.assertEqual(self.queue.avl_tree.root.left.value, 3)
        self.assertEqual(self.queue.avl_tree.root.right.value, 7)

    def test_priority_duplicates(self):
        self.queue.enqueue(3, 3)
        self.queue.enqueue(3, 3)
        self.queue.enqueue(7, 6)
        self.assertEqual(self.queue.avl_tree.root.value, 4)
        self.assertEqual(self.queue.avl_tree.root.left.value, 3)
        self.assertEqual(self.queue.avl_tree.root.right.value, 7)

    def test_empty_tree(self):
        queue = PriorityQueue(None, None)
        value, priority = queue.dequeue()
        self.assertEqual(value, None)
        self.assertEqual(priority, None)


if __name__ == "__main__":
    unittest.main()
