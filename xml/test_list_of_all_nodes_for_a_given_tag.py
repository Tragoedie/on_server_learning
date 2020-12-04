import unittest
import xml.etree.ElementTree as ETree
import os
from on_server_learning.xml.list_of_all_nodes_for_a_given_tag import list_of_nodes

test_demo = os.path.join(os.path.dirname(__file__), 'demo.xml')


class nodes_for_a_given_tag_tests(unittest.TestCase):

    def test_nodes_for_a_given_tag_1(self):
        self.xml_1 = ETree.parse(test_demo)
        self.root = self.xml_1.getroot()
        self.assertEqual(list_of_nodes('name', self.root), [['name', 'Petya']])

    def test_nodes_for_a_given_tag_2(self):
        self.xml_1 = ETree.parse(test_demo)
        self.root = self.xml_1.getroot()
        self.assertEqual(list_of_nodes('', self.root), [])


if __name__ == '__main__':
    unittest.main()
