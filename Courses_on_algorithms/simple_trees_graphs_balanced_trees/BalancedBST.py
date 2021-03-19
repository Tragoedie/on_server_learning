class BSTNode:

    def __init__(self, key, parent):
        self.NodeKey = key  # ключ узла
        self.Parent = parent  # родитель или None для корня
        self.LeftChild = None  # левый потомок
        self.RightChild = None  # правый потомок
        self.Level = 0  # уровень узла


class BalancedBST:

    def __init__(self):
        self.Root = None  # корень дерева

    def GenerateTree(self, a):
        a.sort()
        self.Root = self.recursive_generate(a, 1)

    def recursive_generate(self, a, level):
        if len(a) > 0:
            index_center = len(a) // 2
            node = BSTNode(a[index_center], None)
            node.Level = level
            node.LeftChild = self.recursive_generate(a[:index_center], level + 1)
            node.RightChild = self.recursive_generate(a[index_center + 1:], level + 1)
            if node.LeftChild is not None:
                node.LeftChild.Parent = node
            if node.RightChild is not None:
                node.RightChild.Parent = node
            return node
        else:
            return None

    def IsBalanced(self, root_node):
        left_level = self.get_level(root_node.LeftChild)
        right_level = self.get_level(root_node.RightChild)
        return 0 <= abs(left_level-right_level) <= 1

    def get_level(self, node):
        if node is None:
            return 0
        left_level = self.get_level(node.LeftChild)
        right_level = self.get_level(node.RightChild)
        return max(left_level, right_level, node.Level)
