import xml.etree.ElementTree as ETree


def number_of_xml(attribs, path_to_file):
    xml_1 = ETree.parse(path_to_file)
    root = xml_1.getroot()
    return counter_number_of_xml(attribs, root)


def counter_number_of_xml(attribs, root):
    counter = 0
    if attribs in root.attrib.keys():
        counter += 1
    for j in range(len(root)):
        counter += counter_number_of_xml(attribs, root[j])
    return counter


print(number_of_xml('name', 'demo.xml'))