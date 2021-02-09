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
            return True
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
        return True

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
        if self.Count() == 1:
            self.Root = None
            return True
        if node.Node.RightChild is None:
            if node.Node.LeftChild is not None:
                node.Node.LeftChild.Parent = node.Node.Parent
            if node.Node != self.Root:
                if node.Node.Parent.LeftChild == node.Node:
                    node.Node.Parent.LeftChild = node.Node.LeftChild
                else:
                    node.Node.Parent.RightChild = node.Node.LeftChild
            else:
                self.Root = node.Node.LeftChild
        else:
            if node.Node.LeftChild is None:
                node.Node.RightChild.Parent = node.Node.Parent
                if node.Node != self.Root:
                    if node.Node.Parent.LeftChild == node.Node:
                        node.Node.Parent.LeftChild = node.Node.RightChild
                    else:
                        node.Node.Parent.RightChild = node.Node.RightChild
                else:
                    self.Root = node.Node.RightChild
            else:
                item = node.Node.RightChild
                if item.LeftChild == None:
                    item.Parent = node.Node.Parent
                    item.LeftChild = node.Node.LeftChild
                    if node.Node.LeftChild is not None:
                        node.Node.LeftChild.Parent = item
                    if node.Node != self.Root:
                        if node.Node.Parent.LeftChild == node.Node:
                            node.Node.Parent.LeftChild = node.Node.RightChild
                        else:
                            node.Node.Parent.RightChild = node.Node.RightChild
                    else:
                        self.Root = node.Node.RightChild
                    return True
                while item.LeftChild is not None:
                    item = item.LeftChild
                if item.RightChild is not None:
                    item.RightChild.Parent = item.Parent
                if item.Parent.LeftChild == item:
                    item.Parent.LeftChild = item.RightChild
                else:
                    item.Parent.RightChild = item.RightChild
                item.Parent = node.Node.Parent
                if node.Node.RightChild != item:
                    item.RightChild = node.Node.RightChild
                    node.Node.RightChild.Parent = item
                if node.Node.LeftChild != item:
                    item.LeftChild = node.Node.LeftChild
                    node.Node.LeftChild.Parent = item
                if node.Node != self.Root:
                    if node.Node.Parent.LeftChild == node.Node:
                        node.Node.Parent.LeftChild = item
                    else:
                        node.Node.Parent.RightChild = item
                else:
                    self.Root = item
        return True

    def Count(self):
        return self.putNode(0, self.Root)

    def putNode(self, count, node):
        if node is None:
            return 0
        count += 1
        count += self.putNode(0, node.LeftChild)
        count += self.putNode(0, node.RightChild)
        return count

    def WideAllNodes(self):
        result_nodes = []
        if self.Root is None:
            return result_nodes
        parent_array = [self.Root]
        while len(parent_array) > 0:
            children_array = []
            for node in parent_array:
                result_nodes.append(node)
                if node.LeftChild is not None:
                    children_array.append(node.LeftChild)
                if node.RightChild is not None:
                    children_array.append(node.RightChild)
            parent_array = []
            parent_array.extend(children_array)
        return result_nodes

    def DeepAllNodes(self, order_flag):
        result_nodes = []
        self.put_deep_node(result_nodes, self.Root, order_flag)
        return result_nodes

    def put_deep_node(self, arr, node, flag):
        if node is None:
            return
        if flag == 0:
            self.put_deep_node(arr, node.LeftChild, flag)
            arr.append(node)
            self.put_deep_node(arr, node.RightChild, flag)
        elif flag == 1:
            self.put_deep_node(arr, node.LeftChild, flag)
            self.put_deep_node(arr, node.RightChild, flag)
            arr.append(node)
        elif flag == 2:
            arr.append(node)
            self.put_deep_node(arr, node.LeftChild, flag)
            self.put_deep_node(arr, node.RightChild, flag)


