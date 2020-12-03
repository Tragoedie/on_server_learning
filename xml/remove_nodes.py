import xml.etree.ElementTree as ETree


def remove_nodes(tag, path_to_file):
    xml_1 = ETree.parse(path_to_file)
    root = xml_1.getroot()
    for parent in root.iter():
        for child in parent.findall(tag):
            parent.remove(child)
    xml_1.write(path_to_file)

remove_nodes('pc', 'demo.xml')
