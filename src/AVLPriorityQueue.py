# Рівень 3
# Варіант 2


class Node:
    def __init__(self, value, priority):
        self.left = None
        self.right = None
        self.parent = None
        self.height = 1
        self.value = value
        self.priority = priority


def get_height(node):
    if node is None:
        return 0
    return node.height


class AVLTree:
    def __init__(self, value, priority):
        self.root = Node(value, priority)

    def _left_rotate(self, node):
        new_root = node.right
        node.right = new_root.left
        if new_root.left is not None:
            new_root.left.parent = node
        new_root.parent = node.parent
        if node.parent is None:
            self.root = new_root
        elif node == node.parent.left:
            node.parent.left = new_root
        else:
            node.parent.right = new_root
        new_root.left = node
        node.parent = new_root
        node.height = 1 + max(get_height(node.left), get_height(node.right))
        new_root.height = 1 + max(get_height(new_root.left), get_height(new_root.right))

    def _right_rotate(self, node):
        new_root = node.left
        node.left = new_root.right
        if new_root.right is not None:
            new_root.right.parent = node
        new_root.parent = node.parent
        if node.parent is None:
            self.root = new_root
        elif node == node.parent.right:
            node.parent.right = new_root
        else:
            node.parent.left = new_root
        new_root.right = node
        node.parent = new_root
        node.height = 1 + max(get_height(node.left), get_height(node.right))
        new_root.height = 1 + max(get_height(new_root.left), get_height(new_root.right))

    def _make_balance(self, node):
        while node is not None:
            left_height = get_height(node.left)
            right_height = get_height(node.right)
            node.height = 1 + max(left_height, right_height)
            balance = left_height - right_height
            if balance > 1:
                if get_height(node.left.left) >= get_height(node.left.right):
                    self._right_rotate(node)
                else:
                    self._left_rotate(node.left)
                    self._right_rotate(node)
            elif balance < -1:
                if get_height(node.right.right) >= get_height(node.right.left):
                    self._left_rotate(node)
                else:
                    self._right_rotate(node.right)
                    self._left_rotate(node)
            node = node.parent

    def insert(self, value, priority):
        if self.root is None:
            self.root = Node(value, priority)
            return
        self._insert_recursion_dfs(self.root, value, priority)
        self._make_balance(self.root)

    def _insert_recursion_dfs(self, node, value, priority):
        if priority <= node.priority:
            if node.left is None:
                node.left = Node(value, priority)
                node.left.parent = node
            else:
                self._insert_recursion_dfs(node.left, value, priority)
        else:
            if node.right is None:
                node.right = Node(value, priority)
                node.right.parent = node
            else:
                self._insert_recursion_dfs(node.right, value, priority)

    def print_tree(self, node):
        if node is not None:
            self.print_tree(node.left)
            print(f"{node.value}({node.priority})")
            self.print_tree(node.right)

    def delete_highest_priority(self):
        if self.root is None:
            return None

        current_node = self.root
        while current_node.left:
            current_node = current_node.left

        deleted_node = (current_node.value, current_node.priority)
        if current_node.parent is None:  # Root node
            if current_node.right:
                self.root = current_node.right
                current_node.right.parent = None
            else:
                self.root = None
        else:
            if current_node.right:
                current_node.parent.left = current_node.right
                current_node.right.parent = current_node.parent
            else:
                current_node.parent.left = None

        self._make_balance(current_node.parent)
        return deleted_node


class PriorityQueue:
    def __init__(self, value, priority):
        self.avl_tree = AVLTree(value, priority)

    def enqueue(self, value, priority):
        self.avl_tree.insert(value, priority)

    def dequeue(self):
        return self.avl_tree.delete_highest_priority()

    def is_empty(self):
        return self.avl_tree.root is None
