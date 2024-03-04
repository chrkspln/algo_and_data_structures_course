#   Рівень 3
#   Варіант 1
#   Для заданого бінарного дерева та конкретної вершини в цьому дереві
#   реалізуйте функцію пошуку наступного елемента під час серединного проходу
#   (in-order traversal). Наступник - це вузол, який має значення більше
#   за заданий вузол і знаходиться найближче до нього при серединному обході.
#
#   Нехай у вас задане бінарне дерево такого вигляду:
#
#       10
#      /  \
#     5    15
#    / \     \
#   3   7    20
#            /
#           12
#
#   Для вершини зі значенням 7, наступник - це вузол зі значенням 10.
#   Функція отримує на вхід корінь бінарного дерева та
#   вершину, для якої потрібно знайти наступника.


class BinaryTree:
    def __init__(self, value, left=None, right=None, parent=None):
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent


def find_next(node: BinaryTree) -> BinaryTree:
    if node.right:
        return leftmost_child(node.right)
    else:
        return rightmost_parent(node)


def find_bigger_next_value(tree: BinaryTree, node: BinaryTree) -> BinaryTree:
    next_node = find_next(node)
    while next_node.value <= node.value:
        print(next_node.value, node.value)
        next_node = find_next(next_node)
    return next_node


def leftmost_child(node):
    current = node
    while current.left:
        current = current.left
    return current


def rightmost_parent(node):
    current = node
    while current.parent and current.parent.right == current:
        current = current.parent
    return current.parent


root = BinaryTree(10)
root.left = BinaryTree(5)
root.right = BinaryTree(15)
root.left.parent = root
root.right.parent = root
root.right.right = BinaryTree(20)
root.right.right.parent = root.right
root.right.right.left = BinaryTree(12)

root.right.right.left.parent = root.right.right
root.left.left = BinaryTree(3)
root.left.right = BinaryTree(7)


root.left.left.parent = root.left
root.left.right.parent = root.left


print(find_bigger_next_value(root, root.left).value)