import xml.etree.ElementTree as ETree


def tag_xml(tag, path_to_file):
    xml_1 = ETree.parse(path_to_file)
    root = xml_1.getroot()
    work_massive = []
    tag_xml_recursion(work_massive, root, tag)
    return work_massive


def tag_xml_recursion(work_massive, root, tag):
    if root.tag == tag:
        tag_xml_print(work_massive, root)
    for i in range(len(root)):
        tag_xml_recursion(work_massive, root[i], tag)


def tag_xml_print(work_massive, root):
    if len(root) > 0:
        for j in range(len(root)):
            tag_xml_print(work_massive, root[j])
    else:
        work_massive.append(root.text)


print(tag_xml('languages', 'demo.xml'))
