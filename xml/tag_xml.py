import xml.etree.ElementTree as ETree


def tag_xml(tag):
    xml_1 = ETree.parse('demo.xml')
    root = xml_1.getroot()
    work_massive = []
    for i in range(len(root)):
        if root[i].tag != tag:
            if len(root[i]) > 0:
                for j in range(len(root[i])):
                    if root[i][j].tag == tag:
                        work_massive.append(root[i][j].text)
        else:
            if len(root[i]) > 0:
                for j in range(len(root[i])):
                    work_massive.append(root[i][j].text)
            else:
                work_massive.append(root[i].text)
    return work_massive


print(tag_xml('name'))
