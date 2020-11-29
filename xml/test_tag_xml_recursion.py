import unittest
from on_server_learning.xml.tag_xml_recursion import tag_xml
import xml.etree.ElementTree as ETree


class tag_xml_test(unittest.TestCase):

    def test_tag_equal_1(self):
        self.assertEqual(tag_xml('language', 'demo.xml'), ['9', '7', '8'])

    def test_tag_equal_2(self):
        self.assertEqual(tag_xml('pc', 'demo.xml'), ['Linux', 'Intel Core i7-8700', '64', '5000'])

    def test_tag_equal_3(self):
        self.assertEqual(tag_xml('', 'demo.xml'), [])

    def test_tag_equal_4(self):
        self.assertEqual(tag_xml('item', 'demo.xml'), [])

    def test_tag_equal_5(self):
        xml_1 = ETree.parse('demo.xml')
        root = xml_1.getroot()
        massive = []
        for i in range(len(root[4])):
            if root[4][i].tag == 'pc_item':
                massive.append(root[4][i].text)
        self.assertEqual(tag_xml('pc_item', 'demo.xml'), massive)


if __name__ == '__main__':
    unittest.main()
