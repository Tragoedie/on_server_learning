class BSTNode:

    def __init__(self, key, val, parent):
        self.NodeKey = key  # ключ узла
        self.NodeValue = val  # значение в узле
        self.Parent = parent  # родитель или None для корня
        self.LeftChild = None  # левый потомок
        self.RightChild = None  # правый потомок


class BSTFind:  # промежуточный результат поиска

    def __init__(self):
        self.Node = None  # None если
        # в дереве вообще нет узлов
        self.NodeHasKey = False  # True если узел найден
        self.ToLeft = False  # True, если родительскому узлу надо
        # добавить новый узел левым потомком


class BST:

    def __init__(self, node):
        self.Root = node  # корень дерева, или None

    def FindNodeByKey(self, key):
        node = BSTFind()
        node.Node = self.Root
        while node.Node.NodeKey != key:
            if node.Node.NodeKey > key:
                if node.Node.LeftChild is None:
                    node.ToLeft = True
                    break
                node.Node = node.Node.LeftChild
            else:
                if node.Node.RightChild is None:
                    break
                node.Node = node.Node.RightChild
        else:
            node.NodeHasKey = True
        return node

    def AddKeyValue(self, key, val):
        new_node = BSTNode(key, val, None)
        if self.Root is None:
            self.Root = new_node
            return
        node = self.FindNodeByKey(key)
        if node.NodeHasKey is True:
            return False
        else:
            if node.ToLeft is False:
                node.Node.RightChild = new_node
                new_node.Parent = node.Node
            else:
                node.Node.LeftChild = new_node
                new_node.Parent = node.Node

    def FinMinMax(self, FromNode, FindMax):
        node = FromNode
        if FindMax is False:
            while node.LeftChild is not None:
                node = node.LeftChild
        else:
            while node.RightChild is not None:
                node = node.RightChild
        return node

    def DeleteNodeByKey(self, key):
        node = self.FindNodeByKey(key)
        if node.NodeHasKey is False:
            return False
        if node.Node.RightChild is None:
            if node.Node.LeftChild is not None:
                node.Node.LeftChild.Parent = node.Node.Parent
            if node.Node != self.Root:
                node.Node.Parent.LeftChild = node.Node.LeftChild
            else:
                self.Root = node.Node.LeftChild
        else:
            if node.Node.LeftChild is None:
                node.Node.RightChild.Parent = node.Node.Parent
                if node.Node != self.Root:
                    node.Node.Parent.RightChild = node.Node.RightChild
                else:
                    self.Root = node.Node.RightChild
            else:
                item = node.Node.RightChild
                while item.LeftChild is not None:
                    item = item.LeftChild
                if item.RightChild is not None:
                    item.RightChild.Parent = item.Parent
                    item.Parent.LeftChild = item.RightChild
                item.Parent = node.Node.Parent
                item.RightChild = node.Node.RightChild
                item.LeftChild = node.Node.LeftChild
                if node.Node != self.Root:
                    node.Node.Parent.RightChild = item
                else:
                    self.Root = item

    def Count(self):
        return self.putNode(0, self.Root)

    def putNode(self, count, node):
        if node is None:
            return 0
        count += 1
        count += self.putNode(0, node.LeftChild)
        count += self.putNode(0, node.RightChild)
        return count

