import xml.etree.ElementTree as ETree

xml_1 = ETree.parse('demo.xml')
root = xml_1.getroot()

print(root[3].tag, root[3].text, len(root[3]))
for i in range(len(root[3])):
    print(root[3][i].tag, root[3][i].attrib["name"], root[3][i].text)

computer = root[4]
print(computer.tag, computer.text, len(computer))
for i in range(len(computer)):
    print(computer[i].tag, computer[i].attrib["name"], computer[i].text)
