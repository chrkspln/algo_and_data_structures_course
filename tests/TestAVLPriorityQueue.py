import unittest
from src.AVLPriorityQueue import *


class TestPriorityQueue(unittest.TestCase):
    root = AVLTreeNode(4, 5)
    queue = PriorityQueue(root)

    def test_insertion_and_deletion_normal_case(self):
        node1 = AVLTreeNode(3, 3)
        node2 = AVLTreeNode(7, 6)
        self.queue.enqueue(node1)
        self.queue.enqueue(node2)
        self.assertEqual(self.queue.avl_tree.root.value, 4)
        self.assertEqual(self.queue.avl_tree.root.left.value, 3)
        self.assertEqual(self.queue.avl_tree.root.right.value, 7)

    def test_priority_duplicates(self):
        node1 = AVLTreeNode(3, 3)
        node2 = AVLTreeNode(3, 3)
        node3 = AVLTreeNode(7, 6)
        self.queue.enqueue(node1)
        self.queue.enqueue(node2)
        self.queue.enqueue(node3)
        self.assertEqual(self.queue.avl_tree.root.value, 4)
        self.assertEqual(self.queue.avl_tree.root.left.value, 3)
        self.assertEqual(self.queue.avl_tree.root.right.value, 7)

    def test_empty_tree(self):
        root = AVLTreeNode()
        queue = PriorityQueue(root)
        value, priority = queue.dequeue()
        self.assertEqual(value, None)
        self.assertEqual(priority, None)


if __name__ == "__main__":
    unittest.main()
