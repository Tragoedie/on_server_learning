from on_server_learning.algorithms_1.trees.simple_tree import *


class SimpleTreeNode_with_level(SimpleTreeNode):
    def __init__(self, val, parent, level=None):
        super().__init__(val, parent)
        self.level = level


class SimpleTree_with_level(SimpleTree):

    def level(self):
        self.put_next_level(self.Root, 0)

    def put_next_level(self, node, level):
        node.level = level
        for item in node.Children:
            self.put_next_level(item, level + 1)

