import xml.etree.ElementTree as ETree


def number_of_xml(attribs, path_to_file):
    xml_1 = ETree.parse(path_to_file)
    root = xml_1.getroot()
    counter = [0]
    counter_number_of_xml(attribs, root, counter)
    return counter[0]


def counter_number_of_xml(attribs, root, count):
    if attribs in root.attrib.keys():
        count[0] += 1
    for j in range(len(root)):
        counter_number_of_xml(attribs, root[j], count)


print(number_of_xml('name', 'demo.xml'))