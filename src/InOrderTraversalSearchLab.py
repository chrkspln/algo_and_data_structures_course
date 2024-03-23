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


def find_successor(tree: BinaryTree, node: BinaryTree) -> BinaryTree:
    next_node = next_inorder_node(node)
    while next_node.value <= node.value:
        next_node = next_inorder_node(next_node)
    return next_node.value


def next_inorder_node(node: BinaryTree) -> BinaryTree:
    if node.right:
        return most_left_child(node.right)
    else:
        return find_untraversed_parent(node)


def most_left_child(node):
    curr_node = node
    while curr_node.left:
        curr_node = curr_node.left
    return curr_node


def find_untraversed_parent(node):
    curr_node = node
    while curr_node.parent and curr_node.parent.right == curr_node:
        curr_node = curr_node.parent
    return curr_node.parent
