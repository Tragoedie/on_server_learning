import unittest
import xml.etree.ElementTree as ETree
from on_server_learning.xml.number_of_xml_nodes_7 import number_of_xml


class number_of_xml_tests(unittest.TestCase):

    def test_number_of_xml_equals_1(self):
        self.assertEqual(number_of_xml('name', 'demo.xml'), 7)

    def test_number_of_xml_equals_2(self):
        self.assertEqual(number_of_xml('', 'demo.xml'), 0)

    def test_number_of_xml_equals_3(self):
        xml_1 = ETree.parse('demo.xml')
        root = xml_1.getroot()
        counter = 0
        for i in range(len(root[3])):
            if root[3][i].get("name"):
                counter += 1
        for i in range(len(root[4])):
            if root[4][i].get("name"):
                counter += 1
        self.assertEqual(number_of_xml('name', 'demo.xml'), counter)


if __name__ == '__main__':
    unittest.main()
