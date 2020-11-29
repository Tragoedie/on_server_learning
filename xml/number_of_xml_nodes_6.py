import xml.etree.ElementTree as ETree


def number_of_xml(attribs, path_to_file):
    xml_1 = ETree.parse(path_to_file)
    root = xml_1.getroot()
    return counter_number_of_xml(attribs, root)


def counter_number_of_xml(attribs, root, count=0):
    if attribs in root.attrib.keys():
        count += 1
    for j in range(len(root)):
        count = counter_number_of_xml(attribs, root[j], count)
    return count


print(number_of_xml('name', 'demo.xml'))