import xml.etree.ElementTree as ETree


def list_of_nodes(tag, root):
    massive = []
    for item in root.iter():
        b = []
        if item.tag == tag:
            b.append(item.tag)
            if item.attrib != {}:
                b.append(item.attrib)
            b.append(item.text)
        if b:
            massive.append(b)
    return massive


xml_1 = ETree.parse('demo.xml')
root = xml_1.getroot()
result = list_of_nodes('', root)
if not result:
    print("No nodes with the given tag")
else:
    print(result)
