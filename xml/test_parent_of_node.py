import unittest
import xml.etree.ElementTree as ETree
import os
from on_server_learning.xml.parent_of_node import find_parent_node

test_demo = os.path.join(os.path.dirname(__file__), 'demo.xml')


class find_parent_node_tests(unittest.TestCase):

    def test_find_parent_node_1(self):
        self.xml_1 = ETree.parse(test_demo)
        self.root = self.xml_1.getroot()
        node = self.root[3][0]
        node_parent = self.root[3]
        self.assertEqual(find_parent_node(node, self.root), node_parent)

    def test_find_parent_node_2(self):
        self.xml_1 = ETree.parse(test_demo)
        self.root = self.xml_1.getroot()
        node = self.root
        self.assertEqual(find_parent_node(node, self.root), -1)


if __name__ == '__main__':
    unittest.main()
