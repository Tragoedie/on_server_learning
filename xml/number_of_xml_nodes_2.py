import xml.etree.ElementTree as ETree  # импорт стандарной библиотеки ElementTree


def number_of_xml(attribs, path_to_file):  # название функции
    xml_1 = ETree.parse(path_to_file)  # загрузка в программу xml-документа
    root = xml_1.getroot()  # получение корневого узла
    global counter  # объявление counter глобальной переменной
    counter = 0  # присваивание переменной counter значение равное 0
    counter_number_of_xml(attribs, root)  # вызов рекурсивной функции counter_number_of_xml
    return counter  # возврат значения переменной counter


def counter_number_of_xml(attribs, root):
    if attribs in root.attrib.keys():  # проверка на наличие ключа в словаре
        global counter # указание на то, что будет изменяться глобальная переменная counter
        counter += 1  # если ключ есть, то переменная counter увеличивается на 1
    for j in range(len(root)):  # цикл для перебора узлов
        counter_number_of_xml(attribs, root[j])  # вызов функции counter_number_of_xml для каждого узла


print(number_of_xml('name', 'demo.xml'))
