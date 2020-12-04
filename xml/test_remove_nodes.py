import unittest
import xml.etree.ElementTree as ETree
import os
from on_server_learning.xml.remove_nodes import remove_nodes

test_demo = os.path.join(os.path.dirname(__file__), 'demo.xml')


class find_parent_node_tests(unittest.TestCase):

    def test_remove_nodes_1(self):
        remove_nodes('pc_item', test_demo)
        xml_1 = ETree.parse(test_demo)
        root = xml_1.getroot()
        item = root.find('pc_item')
        self.assertIsNone(item)

    def test_remove_nodes_2(self):
        remove_nodes('pc', test_demo)
        xml_1 = ETree.parse(test_demo)
        root = xml_1.getroot()
        item = root.find('pc')
        self.assertIsNone(item)


if __name__ == '__main__':
    unittest.main()
