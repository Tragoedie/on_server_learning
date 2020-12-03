import xml.etree.ElementTree as ETree


def list_of_nodes(node, root):
    for parent in root.iter():
        for child in range(len(parent)):
            if parent[child] == node:
                return parent


xml_1 = ETree.parse('demo23.xml')
root = xml_1.getroot()
node = root[3][1][0]
print(list_of_nodes(node, root))
