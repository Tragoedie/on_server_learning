import xml.etree.ElementTree as ETree


def find_parent_node(node, root):
    for parent in root.iter():
        for child in range(len(parent)):
            if parent[child] == node:
                return parent
    return -1


xml_1 = ETree.parse('demo.xml')
root = xml_1.getroot()
node = root[3][0]
parent_node = find_parent_node(node, root)
if parent_node == -1:
    print("No parent")
else:
    print(parent_node)