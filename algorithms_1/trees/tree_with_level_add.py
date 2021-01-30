from on_server_learning.algorithms_1.trees.simple_tree import *


class SimpleTreeNode_with_level(SimpleTreeNode):
    def __init__(self, val, parent, level=None):
        super().__init__(val, parent)
        self.level = level


class SimpleTree_with_level(SimpleTree):

    def AddChild(self, ParentNode, NewChild):
        if ParentNode is None:
            ParentNode = self.Root
        if ParentNode is None:
            self.Root = NewChild
            NewChild.level = 0
        else:
            ParentNode.Children.append(NewChild)
            NewChild.Parent = ParentNode
            NewChild.level = ParentNode.level + 1
