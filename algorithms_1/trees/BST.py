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
        # в дереве вообще нету узлов
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

tree = BST(None)
Child_1 = (10, 10)
Child_2 = (4, 4)
Child_3 = (2, 2)
Child_4 = (6, 6)
Child_5 = (20, 20)
Child_6 = (14, 14)
Child_7 = (12, 12)
Child_8 = (17, 17)
Child_9 = (18, 18)
Child_10 = (25, 25)
Child_11 = (23, 23)
Child_12 = (22, 22)
Child_13 = (24, 24)
Child_14 = (28, 28)
Child_15 = (13, 13)
tree.AddKeyValue(Child_1[0], Child_1[1])
tree.AddKeyValue(Child_2[0], Child_2[1])
tree.AddKeyValue(Child_3[0], Child_3[1])
tree.AddKeyValue(Child_4[0], Child_4[1])
tree.AddKeyValue(Child_5[0], Child_5[1])
tree.AddKeyValue(Child_6[0], Child_6[1])
tree.AddKeyValue(Child_7[0], Child_7[1])
tree.AddKeyValue(Child_8[0], Child_8[1])
tree.AddKeyValue(Child_9[0], Child_9[1])
tree.AddKeyValue(Child_10[0], Child_10[1])
tree.AddKeyValue(Child_11[0], Child_11[1])
tree.AddKeyValue(Child_12[0], Child_12[1])
tree.AddKeyValue(Child_13[0], Child_13[1])
tree.AddKeyValue(Child_14[0], Child_14[1])
tree.AddKeyValue(Child_15[0], Child_15[1])
tree.DeleteNodeByKey(10)