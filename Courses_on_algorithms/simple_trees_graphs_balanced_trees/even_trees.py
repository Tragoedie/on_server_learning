class SimpleTreeNode:

    def __init__(self, val, parent):
        self.NodeValue = val  # значение в узле
        self.Parent = parent  # родитель или None для корня
        self.Children = []  # список дочерних узлов


class SimpleTree:

    def __init__(self, root):
        self.Root = root

    def AddChild(self, ParentNode, NewChild):
        if ParentNode is None:
            ParentNode = self.Root
        if ParentNode is None:
            self.Root = NewChild
        else:
            ParentNode.Children.append(NewChild)
            NewChild.Parent = ParentNode

    def DeleteNode(self, NodeToDelete):
        NodeToDelete.Parent.Children.remove(NodeToDelete)
        NodeToDelete.Parent = None

    def GetAllNodes(self):
        node_array = []
        self.putNodeAll(node_array, self.Root)
        return node_array

    def putNodeAll(self, node_array, node):
        node_array.append(node)
        for item in node.Children:
            self.putNodeAll(node_array, item)

    def FindNodesByValue(self, val):
        node_val_array = []
        self.putNodeVal(node_val_array, self.Root, val)
        return node_val_array

    def putNodeVal(self, node_val_array, node, val):
        if node.NodeValue == val:
            node_val_array.append(node)
        for item in node.Children:
            self.putNodeVal(node_val_array, item, val)

    def MoveNode(self, OriginalNode, NewParent):
        self.DeleteNode(OriginalNode)
        self.AddChild(NewParent, OriginalNode)
        # NewParent.Children.append(OriginalNode)
        # OriginalNode.Parent.Children.remove(OriginalNode)
        # OriginalNode.Parent = NewParent

    def Count(self):
        return len(self.GetAllNodes())

    def LeafCount(self):
        return self.putNodeLeaf(0, self.Root)

    def putNodeLeaf(self, count, node):
        if not node.Children:
            count += 1
        for item in node.Children:
            count += self.putNodeLeaf(0, item)
        return count

    def EvenTrees(self):
        number_of_nodes = self.Count()
        if number_of_nodes % 2 or number_of_nodes == 0:
            return []
        return self.EvenTrees_rec(self.Root, None)

    def EvenTrees_rec(self, node, parent_node):
        result = []
        if node.Children is []:
            return result
        number_of_nodes = self.Count_node(node)
        if number_of_nodes % 2 == 0 and parent_node is not None:
            result.append(parent_node)
            result.append(node)
        for child in node.Children:
            result.extend(self.EvenTrees_rec(child, node))
        return result

    def Count_node(self, node):
        return self.count_node_rec(0, node)

    def count_node_rec(self, count, node):
        count += 1
        for item in node.Children:
            count += self.count_node_rec(0, item)
        return count
