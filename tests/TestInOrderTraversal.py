from src.InOrderTraversalSearchLab import BinaryTree, find_successor
import unittest


class InOrderTraversalTest(unittest.TestCase):
    def test_built_in(self):
        root = BinaryTree(10)
        root.left = BinaryTree(5)
        root.right = BinaryTree(15)
        root.left.parent = root
        root.right.parent = root

        root.left.left = BinaryTree(3)
        root.left.right = BinaryTree(7)
        root.left.left.parent = root.left
        root.left.right.parent = root.left

        root.right.right = BinaryTree(20)
        root.right.right.left = BinaryTree(12)
        root.right.right.parent = root.right
        root.right.right.left.parent = root.right.right

        self.assertEqual(find_successor(root, root.left.right), 10, "error!")

    def test_case1(self):
        root = BinaryTree(8)
        root.left = BinaryTree(5)
        root.right = BinaryTree(14)
        root.left.parent = root
        root.right.parent = root

        root.left.left = BinaryTree(4)
        root.left.right = BinaryTree(9)
        root.left.left.parent = root.left
        root.left.right.parent = root.left

        root.right.right = BinaryTree(21)
        root.right.right.left = BinaryTree(10)
        root.right.right.parent = root.right
        root.right.right.left.parent = root.right.right

        self.assertEqual(find_successor(root, root.left.left), 5, "error!")

    def test_case2(self):
        root = BinaryTree(8)
        root.left = BinaryTree(5)
        root.right = BinaryTree(14)
        root.left.parent = root
        root.right.parent = root

        root.left.left = BinaryTree(4)
        root.left.right = BinaryTree(9)
        root.left.left.parent = root.left
        root.left.right.parent = root.left

        root.right.right = BinaryTree(21)
        root.right.right.left = BinaryTree(10)
        root.right.right.parent = root.right
        root.right.right.left.parent = root.right.right

        self.assertEqual(find_successor(root, root.left.right), 14, "error!")


if __name__ == '__main__':
    unittest.main()
