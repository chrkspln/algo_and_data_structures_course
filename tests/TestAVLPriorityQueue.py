import unittest
from src.AVLPriorityQueue import *


class AVLPriorityQueueTest(unittest.TestCase):

    def test_enqueue(self):
        node = AVLTreeNode(10, 5)
        queue = PriorityQueue(node)
        node1 = AVLTreeNode(6, 3)
        queue.enqueue(node1)
        node2 = AVLTreeNode(2, 1)
        queue.enqueue(node2)
        node3 = AVLTreeNode(7, 2)
        queue.enqueue(node3)
        node4 = AVLTreeNode(8, 4)
        queue.enqueue(node4)
        node5 = AVLTreeNode(1, 0)
        queue.enqueue(node5)
        node6 = AVLTreeNode(3, 6)
        queue.enqueue(node6)
        node7 = AVLTreeNode(12, 2)
        queue.enqueue(node7)
        node8 = AVLTreeNode(5, 7)
        queue.enqueue(node8)

        queue.print_queue()

    def test_dequeue(self):
        node = AVLTreeNode(10, 5)
        queue = PriorityQueue(node)
        node1 = AVLTreeNode(6, 3)
        queue.enqueue(node1)
        node2 = AVLTreeNode(2, 1)
        queue.enqueue(node2)
        node3 = AVLTreeNode(7, 2)
        queue.enqueue(node3)
        node4 = AVLTreeNode(8, 4)
        queue.enqueue(node4)
        node5 = AVLTreeNode(1, 0)
        queue.enqueue(node5)
        node6 = AVLTreeNode(3, 6)
        queue.enqueue(node6)
        node7 = AVLTreeNode(12, 2)
        queue.enqueue(node7)
        node8 = AVLTreeNode(5, 7)
        queue.enqueue(node8)

        queue.dequeue()
        queue.dequeue()
        queue.dequeue()
        queue.dequeue()

        queue.print_queue()
