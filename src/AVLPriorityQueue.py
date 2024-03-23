#   Рівень 3
#   Варіант 2
#
#   Реалізуйте структуру даних "черга з пріоритетами" на основі  AVL-дерева,
#   в якому  батьківський елемент має вищий пріоритет, ніж елемент справа,
#   або нижчий або рівний пріоритет, ніж пріоритет його лівої дитини.
#
#   Операції, які підтримує ваша черга:
#
#   1. Вставка елемента з заданим значенням та пріоритетом до черги.
#   2. Видалення та повернення елемента з найвищим пріоритетом з черги.
#   3. Перегляд черги без її зміни.
#
#   Для реалізації такої черги з пріоритетами слід використати
#   окремий клас `Node`, де кожен елемент буде мати два поля: значення та пріоритет.
#   При вставці елемента до черги, його потрібно розмістити
#   у відповідному порядку з урахуванням пріоритету.


class AVLTreeNode:
    def __init__(self, value=None, priority=None):
        self.parent = None
        self.right = None
        self.left = None
        self.value = value
        self.priority = priority
        self.height = 1
        self.balance = 0


class AVLTree:
    def __init__(self, node: AVLTreeNode):
        self.root = node

    def update_height(self, node: AVLTreeNode):
        if not node:
            return

        start = node
        while start:
            if start.left is not None:
                if start.right is not None:
                    start.height = 1 + max(start.left.height, start.right.height)
                else:
                    start.height = 1 + start.left.height
            elif start.right is not None:
                start.height = 1 + start.right.height
            else:
                start.height = 1

            start = start.parent

    def insert_element(self, root: AVLTreeNode, node: AVLTreeNode):
        if not root:
            return

        if node.priority <= root.priority:
            if not root.left:
                root.left = node
                node.parent = root
            else:
                self.insert_element(root.left, node)
        elif node.priority > root.priority:
            if not root.right:
                root.right = node
                node.parent = root
            else:
                self.insert_element(root.right, node)

            self.update_height(node)

        while node:

            node.balance = (node.left.height - node.right.height if node.left and node.right else 1)
            if root.balance in [-1, 0, 1]:
                node = node.parent
            else:
                # rl-case
                if node.balance < -1 and node.priority < node.right.priority:
                    self.rlcase(node)
                # rr-case
                if node.balance < -1 and node.priority > node.right.priority:
                    self.left_rotation(node)
                # lr-case
                if node.balance > 1 and node.priority > node.right.priority:
                    self.lrcase(node)
                # ll-case
                if node.balance > 1 and node.priority < node.right.priority:
                    self.right_rotation(node)

    def right_rotation(self, node: AVLTreeNode):
        z = node
        y = z.left
        x = y.left
        p = z.parent
        temp = None

        if y.right:
            temp = y.right

        if p:
            if p.left == z:
                p.left = y
            else:
                p.right = y

        y.right = z
        z.parent = y
        if temp:
            z.left = temp

        if not p:
            self.root = y
            y.parent = None

        self.update_height(x)
        self.update_height(y)
        self.update_height(z)

    def left_rotation(self, node: AVLTreeNode):
        z = node
        y = z.right
        x = y.right
        p = z.parent
        temp = None

        if y.left:
            temp = y.left

        if p:
            if p.left == z:
                p.left = y
            else:
                p.right = y

        y.left = z
        z.parent = y
        if temp:
            z.right = temp

        if not p:
            self.root = y
            y.parent = None

        self.update_height(x)
        self.update_height(y)
        self.update_height(z)

    def rrcase(self, node: AVLTreeNode):
        self.left_rotation(node)

    def llcase(self, node: AVLTreeNode):
        self.right_rotation(node)

    def lrcase(self, node: AVLTreeNode):
        z = node
        y = z.left
        x = y.right
        p = z.parent
        temp = None

        if x.right:
            temp = x.right

        z.left = x
        x.parent = z
        z.left = y

        if temp:
            y.right = temp

        self.right_rotation(node)
        self.update_height(y)

    def rlcase(self, node: AVLTreeNode):
        z = node
        y = z.right
        x = y.left
        p = z.parent
        temp = None

        if x.left:
            temp = x.left

        z.right = x
        x.parent = z
        z.right = y

        if temp:
            y.left = temp

        self.left_rotation(node)
        self.update_height(y)

    def delete_element(self, root: AVLTreeNode):
        if not root:
            return

        node = root
        parent = None
        while node.left:
            parent = node.parent
            node = node.left

        find_node = node
        if node == root:
            if root.right:
                root.right = root
                root.parent = None
        if node.right:
            node.right.parent = node.parent
            node.parent.left = node.right
        else:
            if node.parent is not None:
                node.parent.left = None

        node = root
        while node:
            self.update_height(node)
            node.balance = (node.left.height - node.right.height if node.left and node.right else 0)

            if root.balance in [-1, 0, 1]:
                node = node.parent
            else:
                # rl-case
                if node.balance < -1 and node.priority < node.right.priority:
                    self.rlcase(node)
                # rr-case
                if node.balance < -1 and node.priority > node.right.priority:
                    self.left_rotation(node)
                # lr-case
                if node.balance > 1 and node.priority > node.right.priority:
                    self.lrcase(node)
                # ll-case
                if node.balance > 1 and node.priority < node.right.priority:
                    self.right_rotation(node)

        return find_node.value, find_node.priority

    def tree_print(self, root):
        if not root:
            return

        self.tree_print(root.left)
        print("value: " + str(root.value) + " priority: " + str(root.priority))
        self.tree_print(root.right)


class PriorityQueue:
    def __init__(self, node: AVLTreeNode):
        self.avl_tree = AVLTree(node)

    def enqueue(self, node: AVLTreeNode):
        self.avl_tree.insert_element(self.avl_tree.root, node)

    def dequeue(self):
        if self.avl_tree.root:
            max_priority_node = self.avl_tree.delete_element(self.avl_tree.root)
            return max_priority_node
        return

    def print_queue(self):
        self.avl_tree.tree_print(self.avl_tree.root)
